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

    def set_patients(self, patients):
        self.cmds_ts.clear()
        for p in patients:
            new_row = (p, p.lastname, p.firstname, str(p.dob), p.recordno)
            self.cmds_ts.append(new_row)

    # TODO add selected signal
