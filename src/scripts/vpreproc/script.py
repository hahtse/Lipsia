    def generateScript(self):
        scriptName = QtGui.QFileDialog.getSaveFileName(self, "Save Shell script", self.homePath, ("*.sh"))
        regExp = QtCore.QRegExp(QtCore.QString("*.sh"))
        regExp.setPatternSyntax(QtCore.QRegExp.Wildcard)
        if(not scriptName.isEmpty()):
            if not regExp.exactMatch(scriptName):
                scriptName.append('.sh')
            self.script = open(scriptName, 'w')
            os.system(str("chmod +x " + scriptName))
            self.script.write("#! /bin/sh\n\n")
        else:
            self.throwError("Please specify a scriptname")
        script.write("\nanzahl="+str(self.myFileList.length())
        i = 1
        for file in self.myFileList:
            script.write("f"+str(i)+"="+str(file))
            i+=1

        script.write("\ni=1\nwhile [ $i -le "+str(anzahl)+" ]\ndo")
        
        script.write("\ndone")
        if self.ui.cb_atlas_registration.isChecked():
            self.script.write("\n ")
        if self.ui.cb_create_mask.isChecked():
            self.script.write("\n ")
        if self.ui.cb_debug_output.isChecked():
            self.script.write("\n ")
        if self.ui.cb_fieldmap_correction.isChecked():
            self.script.write("\n ")
        if self.ui.cb_high_pass.isChecked():
            self.script.write("\n ")
        if self.ui.cb_low_pass.isChecked():
            self.script.write("\n ")
        if self.ui.cb_movement_correction.isChecked():
            outFile = str(self.output_dir).rstrip("/") + "/movcorr_" + file.split("/")[len(file.split("/"))-1]
            self.script.write("\nvmovcorrection -in " + str(file) + " -out " + str(outFile)")
        if self.ui.cb_set_repetition.isChecked():

            self.script.write("\n ")
        if self.ui.cb_show_mask.isChecked():
            self.script.write("\n ")
        if self.ui.cb_show_registration_results.isChecked():
            self.script.write("\n ")
        if self.ui.cb_slicetime_correction.isChecked():
            self.script.write("\n ")
        if self.ui.cb_spatial_filtering.isChecked():
            outFile = str(self.output_dir).rstrip("/") + "/sfilter_" + file.split("/")[len(file.split("/"))-1]
            self.script.write("\nvpreprocess -in " + file + " -out " + outFile + " -fwhm " + str(self.ui.sb_fwhm.value()))        
        if self.ui.cb_temporal_filtering.isChecked():
            self.script.write("\n ")
        if self.ui.cb_write_logfile.isChecked():
            self.script.write("\n ")
        if self.ui.sb_fwhm.value():
            self.script.write("\n ")
        if self.ui.sb_hp_cutoff.value():
            self.script.write("\n ")
        if self.ui.sb_lp_cutoff.value():
            self.script.write("\n ")
        if self.ui.sb_max_num_voxel.value():
            self.script.write("\n ")
        if self.ui.rb_create_average_mask.isChecked():
            self.script.write("\n ")
        if self.ui.rb_create_mask_subject.isChecked():
            self.script.write("\n ")
        if self.ui.dsb_repetition_time.value():
            self.script.write("\n ")
        if self.ui.le_directory.text():
            self.script.write("\n ")
        if self.ui.le_prefix.text():
            self.script.write("\n ")
        if self.ui.comboBox_template.currentIndex():
            self.script.write("\n ")
        if self.ui.comboBox_template.currentText():
            self.script.write("\n ")
        if self.ui.cb_rigid_registration.isChecked():
            self.script.write("\n ")
        if self.ui.sb_max_iterations_p1.value():
            self.script.write("\n ")
        if self.ui.cb_prealign_images.isChecked():
            self.script.write("\n ")
        if self.ui.cb_affine_registration.isChecked():
            self.script.write("\n ")
        if self.ui.sb_max_iterations_p2.value():
            self.script.write("\n ")
        if self.ui.cb_deformable_registration.isChecked():
            self.script.write("\n ")
        if self.ui.sb_max_iterations_p3.value():
            self.script.write("\n ")
        if self.ui.sb_max_deformation.value():
            self.script.write("\n ")
        if self.ui.comboBox_interpol_func.currentIndex():
            self.script.write("\n ")
        if self.ui.le_output_resolution.text():
            self.script.write("\n ")
