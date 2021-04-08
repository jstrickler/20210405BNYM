from datetime import date


class President():
    def __init__(self, index):
        try:
            int_index = int(index)
        except (TypeError, ValueError) as err:
            raise err
        else:
            self._get_data(int_index)

    @staticmethod
    def _mkdate(raw_date):
        if raw_date != "NONE":
            raw_year, raw_month, raw_day = raw_date.split('-')
            d = date(int(raw_year), int(raw_month), int(raw_day))
        else:
            d = None

        return d

    def hello(self):
        print(f"Hello from {self.first_name} {self.last_name}")

    def _get_data(self, index):
        with open("DATA/presidents.txt") as pfile:
            for line in pfile:
                flds = line.rstrip().split(":")

                if int(flds[0]) == int(index):
                    self._term = index
                    self._lname = flds[1]

                    self._fname = flds[2]

                    self._bdate = self._mkdate(flds[3])
                    self._ddate = self._mkdate(flds[4])

                    self._bplace = flds[5]
                    self._bstate = flds[6]

                    self._ts_date = self._mkdate(flds[7])
                    self._te_date = self._mkdate(flds[8])

                    self._party = flds[9]

                    break
            else:
                raise ValueError("Invalid term number")

    @property
    def term(self):
        return self._term

    @property
    def last_name(self):
        return self._lname

    @property
    def first_name(self):
        return self._fname

    @property
    def birth_date(self):
        return self._bdate

    @property
    def death_date(self):
        return self._ddate

    @property
    def birth_place(self):
        return self._bplace

    @property
    def birth_state(self):
        return self._bstate

    @property
    def term_start_date(self):
        return self._ts_date

    @property
    def term_end_date(self):
        return self._te_date

    @property
    def party(self):
        return self._party

    @party.deleter
    def party(self):
        del self._party

    def __str__(self):
        return f"President <{self.first_name} {self.last_name}:{self.term}>"