


class MailMerge():
    def __init__(self):
        self.name = "%name%"
        self.list_of_names = []
        self.template = "Letters/_template.txt"
        self.index = 0
        

    def write_letter(self):
        self.get_names()
        for self.index in range(len(self.list_of_names)-1):
            filename = "/home/caboose/codingProjects/python/udemy/Day24 - filesystem/ReadyToSend/Letter For " + self.list_of_names[self.index].strip() + ".txt"

            with open(filename.strip('\n').strip('\r'), "w+") as letter_for:
                with open(file=self.template, mode="r") as letter_template:
                    for line in letter_template:
                        if self.name in line:
                            line = line.replace(self.name, self.list_of_names[self.index].strip('\r').strip('\n'))

                        letter_for.write(line)
                    

    def get_names(self):
        with open ("Names/invited_names.txt", "r") as file_names:
            for name in file_names:
                self.list_of_names.append(name)


if __name__ == "__main__":
    mail = MailMerge()
    mail.get_names()
    mail.write_letter()