import gobject
import gtk

class PatientSelector(gtk.TreeView):
    def __init__(self):
        cmds_ts = gtk.ListStore(gobject.TYPE_PYOBJECT,
                gobject.TYPE_STRING, # Last name
                gobject.TYPE_STRING, # First name
                gobject.TYPE_STRING, # DoB
                gobject.TYPE_INT, # Recordno
                )

        gtk.TreeView.__init__(self, cmds_ts)

        self.cmds_ts = cmds_ts
        self.cmds_tv = self

        generic_tr = gtk.CellRendererText ()

        cols = []
        col = gtk.TreeViewColumn("Lastname", generic_tr, text=1)
        col.set_sort_column_id(1)
        cols.append(col)

        col = gtk.TreeViewColumn("Firstname", generic_tr, text=2)
        col.set_sort_column_id(2)
        cols.append(col)

        col = gtk.TreeViewColumn("DoB", generic_tr, text=3)
        col.set_sort_column_id(3)
        cols.append(col)

        col = gtk.TreeViewColumn("Recordno", generic_tr, text=4)
        col.set_sort_column_id(4)
        cols.append(col)

        for col in cols:
            col.set_resizable (True)
            self.cmds_tv.append_column (col)

        self.cmds_tv.connect("row-activated", self.__on_row_activated)

    def set_patients(self, patients):
        self.cmds_ts.clear()
        for p in patients:
            new_row = (p, p.lastname, p.firstname, str(p.dob), p.recordno)
            self.cmds_ts.append(new_row)

    def __on_row_activated(self, treeview, path, column):
        iter = self.cmds_ts.get_iter(path)
        patient = self.cmds_ts.get_value(iter, 0)
        if patient:
            self.emit("patient-selected", patient)

    def get_patient_at_cursor(self):
        path, column = self.cmds_tv.get_cursor()
        if path is None:
            return None
        iter = self.cmds_ts.get_iter(path)
        return self.cmds_ts.get_value(iter, 0)

gobject.type_register(PatientSelector)
gobject.signal_new("patient-selected", PatientSelector, 
        gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, (gobject.TYPE_PYOBJECT,))
