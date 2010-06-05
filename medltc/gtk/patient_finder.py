import gobject
import gtk

import medltc.django
from medltc.django.models.patient import Patient

from .patient_selector import PatientSelector

class PatientFinder(gtk.Frame):
    def __init__(self):
        gtk.Frame.__init__(self)
        hpane = gtk.HPaned()
        self.add(hpane)

        self.min_firstname_length = 3
        self.min_lastname_length = 3

        self.lastname_te = gtk.Entry()
        self.firstname_te = gtk.Entry()
        self.recordno_te = gtk.Entry()

        self.lastname_te.connect("changed", self.__on_lastname_te_changed)
        self.firstname_te.connect("changed", self.__on_firstname_te_changed)
        self.recordno_te.connect("changed", self.__on_recordno_te_changed)

        self.prev_lastname_search = None
        self.prev_firstname_search = None
        self.prev_recordno_search = None

        table = gtk.Table(3, 2, False)
        table.attach(gtk.Label("Lastname"), 0, 1, 0, 1, yoptions = 0)
        table.attach(gtk.Label("Firstname"), 0, 1, 1, 2, yoptions = 0)
        table.attach(gtk.Label("Recordno"), 0, 1, 2, 3, yoptions = 0)
        table.attach(self.lastname_te, 1, 2, 0, 1, yoptions = 0)
        table.attach(self.firstname_te, 1, 2, 1, 2, yoptions = 0)
        table.attach(self.recordno_te, 1, 2, 2, 3, yoptions = 0)
        hpane.pack1(table)

        self.selector = PatientSelector()
        sw = gtk.ScrolledWindow ()
        sw.set_policy (gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw.add (self.selector)
        hpane.pack2(sw, resize = True)

        self.selector.connect("patient-selected", self.__on_patient_selected)

    def __find_patients(self):
        ln = self.lastname_te.get_text().upper()
        fn = self.firstname_te.get_text().upper()
        rn = self.recordno_te.get_text()

        if len(ln) < self.min_lastname_length and \
           len(fn) < self.min_firstname_length:
           self.selector.set_patients([])
           return

        patients = Patient.objects.all()
        if ln:
            patients = patients.filter(lastname__startswith = ln)
        if fn:
            patients = patients.filter(firstname__startswith = fn)
        self.selector.set_patients(patients)

    def __on_lastname_te_changed(self, te):
        self.__find_patients()

    def __on_firstname_te_changed(self, te):
        self.__find_patients()

    def __on_recordno_te_changed(self, te):
        self.__find_patients()

    def __on_patient_selected(self, pfinder, patient):
        self.emit("patient-selected", patient)

    def get_patient_at_cursor(self):
        return self.selector.get_patient_at_cursor()

gobject.type_register(PatientFinder)
gobject.signal_new("patient-selected", PatientFinder, 
        gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, (gobject.TYPE_PYOBJECT,))

if __name__ == "__main__":
    def on_patient_selected(pfinder, patient):
        print "PatientFinder selected %s, %s (%d)" % \
                (patient.lastname, patient.firstname, patient.recordno)

    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_default_size(600, 400)
    window.set_title("PatientFinder")
    window.connect("delete_event", lambda *a: gtk.main_quit())
    pfinder = PatientFinder()
    window.add(pfinder)
    window.show_all()
    pfinder.connect("patient-selected", on_patient_selected)
    gtk.main()

