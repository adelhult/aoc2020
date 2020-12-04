import re

class Passport:
    def __init__(self, fields):
        """
        Given a string of whitespace
        seperated kv-pairs create a Passport
        """

        for field in fields.split():
            k, v = field.split(":")
            
            if k == "byr":  
                self.byr = v
            elif k == "iyr":
                self.iyr = v
            elif k == "eyr":
                self.eyr = v
            elif k == "hgt":
                self.hgt = v
            elif k == "hcl":
                self.hcl = v
            elif k == "ecl":
                self.ecl = v
            elif k == "pid":
                self.pid = v
            elif k == "cid":
                self.cid = v

    @staticmethod
    def read(document) -> list:
        """Iterate over a doc with passport data"""
        entries = re.split("^\\n", document, flags=re.MULTILINE)
        for entry in entries:
            kvs_string = entry.replace("\n", " ")
            yield Passport(kvs_string)
    
    def valid(self) -> bool:
        """Checks if a passport is valid"""
        try:
            return (
                # valid years
                1920 <= int(self.byr) <= 2002 and
                2010 <= int(self.iyr) <= 2020 and
                2020 <= int(self.eyr) <= 2030 and

                # correct length:
                (  
                    (
                        self.hgt[-2:] == "cm" and
                        150 <= int(self.hgt[:-2]) <= 193) or
                    (
                        self.hgt[-2:] == "in" and
                        59 <= int(self.hgt[:-2]) <= 76
                    )
                ) and

                # hair color starts with a "#"
                self.hcl[0] == "#" and
                # ... is 7 chars long
                len(self.hcl) == 7 and
                # ... and in hex fomat
                int(self.hcl[1:], 16) >= 0 and

                # is one of the given colors
                self.ecl in ["amb", "blu", "brn",
                             "gry", "grn", "hzl", "oth"] and 
                
                # 9 digits long:
                len(self.pid) == 9 and
                # ...and contains only numbers
                self.pid.isdigit()
            )

        except Exception:
            return False
    
    def __repr__(self):
        return f"<Passport, id: {self.pid}>"