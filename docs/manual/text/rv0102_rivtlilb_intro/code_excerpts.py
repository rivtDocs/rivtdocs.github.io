    def t_read(self, tL: str) -> str:
        """[summary]
        
        Args:
            tl (str): [description]
        """
        locals().update(self.rivetD)
        
        df = tL[1].strip()
        filenameS = tL[2].strip()
        pnameS = str(Path(self.folderD["tpath"], filenameS).as_posix())
        pnameS 
        cmdS = str(df) + "= pd.read_csv('" + pnameS + "')" 
        exec(cmdS)     
        
        self.rivetD.update(locals())

    def t_save(self, tL: str):
        """[summary]
        
        Args:
            tL (str): [description]
        """

        locals().update(self.rivetD)

        dfS = tL[1].strip()
        eval(dfS)
        filenameS = tL[2].strip()
        if ".csv" in filenameS:
            pathnameS =  Path(self.folderD["tpath"], filenameS ).as_posix()
            cmdlineS =  dfS + ".to_csv('" + str(pathnameS) +  "',index = False)"
            exec(cmdlineS)
        elif ".png" or ".jpg" in filenameS:
            pathnameS =  Path(self.folderD["fpath"], filenameS ).as_posix()
            cmdline1 = "fig =" + dfS + ".get_figure()"
            cmdline2 =  "fig.savefig('" + str(pathnameS) +  "')"
            exec(cmdline1)
            exec(cmdline2) 

        self.rivetD.update(locals())
        
    def t_data(self, tL:str) -> str:
        """[summary]
        
        Args:
            tLine (str): [description]
        """
        locals().update(self.rivetD)

        dfS = tL[1].strip()
        cmdlineS = dfS + " = pd.DataFrame()"
        exec(cmdlineS)        
    
        self.rivetD.update(locals())

    def t_table(self, tL: list):
        """insert table from inline or csv, rst file 
        
        Args:
            ipl (list): parameter list
        """       
        locals().update(self.rivetD)
        
        try:
            widthI = int(tL[0].split(":")[1])
        except:
            widthI = int(self.setcmdD["cwidth"])
        self.setcmdD.update({"cwidth":widthI})
        tableS = ""; utfS = ""
        files = tL[1].strip()
        tfiles = Path(self.folderD["tpath"], files)   
        if ".csv" in tL[1]:                        # csv ftLe       
            format1 = []
            with open(tfiles,'r') as csvfiLe:
                readL = list(csv.reader(csvfiLe))
            for row in readL:
                wrow=[]
                for i in row:
                    templist = textwrap.wrap(i, widthI) 
                    wrow.append("""\n""".join(templist))
                format1.append(wrow)
            sys.stdout.flush()
            old_stdout = sys.stdout
            output = StringIO()
            output.write(tabulate(format1, tablefmt="grid", headers="firstrow"))            
            utfS = output.getvalue()
            titleS = "  \n"
            sys.stdout = old_stdout
            try: titleS = tL[2].strip() + titleS
            except: pass        
        print(utfS); self.calcS += utfS + "\n"  
    
    def t_plot(self, tL: str)-> list:
        """[summary]
        
        Args:
            tL (str): [description]
        """                
 
        locals().update(self.rivetD)
        
        pltL = tL[1].split(",")
        dfS, pltS = pltL[0].strip(),pltL[1].strip()
        pltcmd = tL[2].strip()
        cmdline1 = "ax = plt.gca()"
        cmdline2 = pltS + "=" + dfS + ".plot(" + pltcmd + ", ax=ax)"
        exec(cmdline1)
        exec(cmdline2)

        self.rivetD.update(locals())

    def t_add(self, tL: str)-> list:
        """[summary]
        
        Args:
            tL (str): [description]
        """                

        locals().update(self.rivetD)

        pltL = tL[1].split(",")
        dfS, pltS = pltL[0].strip(),pltL[1].strip()
        pltcmd = tL[2].strip()
        cmdline2 = pltS +"=" + dfS + ".plot(" + pltcmd + ", ax=ax)"
        exec(cmdline2)

        self.rivetD.update(locals())

    def t_image(self, tL: list):
        """insert image from fiLe
        
        Args:
            ipl (list): parameter list
        """
        try:
            scaleI = int(tL[2].strip())
        except:
            scaleI = self.setcmdD["scale1"]
        self.setcmdD.update({"scale1":scaleI})
        self.setsectD["fnum"] += 1
        figI = self.setsectD["fnum"]
        sectI = self.setsectD["snum"]
        files = tL[1].strip()
        try:
            captionS = tL[2].strip()
            imgpathS = str(Path(self.folderD["fpath"], files))
            utfS = ("Figure " + str(sectI) + '.' + str(figI) + "  "  
               + captionS + "\npath: " + imgpathS + "\n")
        except:
            imgpathS = str(Path(self.folderD["fpath"], files))
            utfS = ("Figure: " + imgpathS + "\n")
        print(utfS); self.calcS += utfS + "\n"

    def t_image2(self, tL: list):
        """insert two images side by side from fiLes
        
        Args:
            tL (list): image parameter list
        """
        try:                                            # update default scale
            scaleI= tL[2].strip()
            scale1I = int(scaleI.split(","))[0].strip()
            scale2I = int(scaleI.split(","))[1].strip()
            self.setcmdD.update({"scale1":scale1I})
            self.setcmdD.update({"scale2":scale2I})
        except:
            scale1I = self.setcmdD["scale1"]
            scale2I = self.setcmdD["scale2"]
        self.setsectD["fnum"] += 1                     # image 1
        figI = self.setsectD["fnum"]
        sectI = self.setsectD["snum"]
        files = tL[1].strip()
        captionS = tL[3].strip()
        imgP = str(Path(self.folderD["fpath"], files))
        utfS = ("Figure " + str(sectI) + '.' + str(figI) + "  "  
               + captionS + "\npath: " + imgP)
        print(utfS); self.calcS += utfS + "\n"

        self.setsectD["fnum"] += 1                     # image 2
        figI = self.setsectD["fnum"]
        sectI = self.setsectD["snum"]
        files = tL[2].strip()
        captionS = tL[4].strip()
        imgP = str(Path(self.folderD["fpath"], files))
        utfS = ("Figure " + str(sectI) + '.' + str(figI) + "  "  
               + captionS + "\npath: " + imgP)
        print(utfS); self.calcS += utfS + "\n"