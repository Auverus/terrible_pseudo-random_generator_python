class customMSM:

    seed = 1234567890
    digits = 10
    repeatee = 0
    #some functions to help life
    def write_line(self, append):
        output = []
        inn = open('seed_his','r')
        for i in inn:
            output.append(i)
        for i in append:
            output.append(i)
        inn.close()
        inn = open('seed_his','w')
        inn.truncate()
        output = map(lambda s: s.strip(), output)
        for i in output:
            inn.write(i)
            inn.write("\n")

        inn.close()

    ##Reading seed value from file if exists.
    def get_seed(self):
        try:
            seed_file = open('seed', 'r')
            data = seed_file.readline()
            seed_file.close
            if len(data) > customMSM.digits:
                data = strip(data[:customMSM.digits])
            customMSM.seed = int(data)
        except:
            pass
    
    ##Modification of seed value
    def generate_new_seed(self):
        customMSM.seed = str(customMSM.seed * customMSM.seed)
        while len(customMSM.seed) < customMSM.digits * 2:
            customMSM.seed = '1' + customMSM.seed
        start = int(customMSM.digits / 2)
        end = start + customMSM.digits
        customMSM.seed = int(customMSM.seed[start:end])
    
    ##This function returns a random number between 0 and limit, with 0 inclusive and limit exclusive.
    def random(self, limit):
        self.check_seed()
        self.get_seed()
        self.seed_his()
        self.check_line()
        for i in range(0,25000):
            self.generate_new_seed()
        selection = customMSM.seed % limit      ##I chose % as it maintains equal biasnes towards all the possible output numbers.
        customMSM.seed += selection             ##To try reduce repeatitive patterns.
        file = open('seed', 'w')                ##Saving seed value to file for more randomized value and to reduce chance of producing same number at each execution with same input condition.
        file.write(str(customMSM.seed))
        file.close
        return selection
    
    def check_seed(self):
        count = 0
        try:
            data = open('seed','r')
            #print(data)
            for i in data:
                count = i.count('0')
                print(i)
                print(count)
            if count > 0:
                #remove zeros from data
                data = open('seed','w')
                for a in range(count):
                    print(a)
                    datas = i.replace("0","")
                print(datas)
                customMSM.repeatee = datas
                data.truncate()
                data.write(datas)
                data.close
                pass
            else:
                data.close
        except(FileNotFoundError):
            self.get_seed
    
    def seed_his(self):
        count = 0
        try:
            his = open('seed_his','r')
            his.close
        except(FileNotFoundError):
            his = open('seed_his','w')
            his.truncate()
            his.close
        his = open('seed_his','r')
        line_count = 0
        for line in his:
            if line != "\n":
                line_count += 1
        his.close()
        print("line_count: ",line_count)
        if line_count > 1:
            his = open('seed_his','r')
            firstline = his.readlines()[0].rstrip()
            his.close
            with open('seed_his') as search:
                countl=0
                igg = 0
                list = []
                for line in search:
                    line = line.rstrip()  # remove '\n' at end of line
                    #print "Line", line
                    list.append(line)
                    igg = igg + 1
                    if "96251" in line: #"96251"
                        #print(line )
                        countl+=1
                    if "2721" in line: #"2721"
                        #print(line )
                        countl+=1
                    if "8481" in line:
                        countl+=1
                    if str(customMSM.repeatee) in line:
                        countl+=1
            if countl > 1:
                tmp = []
                appends = []
                with open('seed_his') as cal:
                    for i in cal:
                        tmp.append(i)
                new_seed = ((int(tmp[-0]) + int(tmp[-1]))*int(tmp[-2]))/int(tmp[-3])
                data = open('seed','r')
                # for i in data:
                #     new_seed.append(i)
                data.close
                his_e = open('seed_his','w')
                his_e.truncate()
                his_e.close
                his = open('seed','w')
                his.write(str(new_seed))
                his.close
                customMSM.seed = int(new_seed)
            else:
                out = []
                try:
                    data = open('seed','r')
                    for i in data:
                        out.append(i)
                    data.close
                    self.write_line(out)
                except(FileNotFoundError):
                    self.get_seed()                                    
        else:
            out = []
            try:
                data = open('seed','r')
                for i in data:
                    out.append(i)
                data.close
                self.write_line(out)
            except(FileNotFoundError):
                self.get_seed()
    def check_line(self):
        count = 0
        with open("seed_his", 'r') as fp:
            for count, line in enumerate(fp):
                pass
        if count > 150:
            edit = open("seed_his", 'w')
            edit.truncate()
            edit.close()