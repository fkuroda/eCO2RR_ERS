import matplotlib
import json
import glob
import sys
import os

sys.path.append("/vol0403/data/hp230205/u10028/QE_TOOLS_C2_selective/src/output_reader")
import qe_structure_output 
import qe_parameter_result_output 
#print(sys.path)
#set_dict={"QFCC_CYCLE1_100":["hollow_C_1_1","hollow_C_1_2","hollow_C_2_1","hollow_C_2_2","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"QFCC_CYCLE1_010":["hollow_C_1_1","hollow_C_1_2","hollow_C_2_1","hollow_C_2_2","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"QFCC_CYCLE1_001":["hollow_C_1_1","hollow_C_1_2","hollow_C_2_1","hollow_C_2_2","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
set_dict={"QBCC_CYCLE3_110":["hollow_C_1_1","hollow_C_1_2","hollow_C_1_3","hollow_C_1_4","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_1_3","ontop_CO_1_4","slab_1"]}
#set_dict={"QBCC_CYCLE3_100":["hollow_C_1_1","hollow_C_1_2","hollow_C_2_1","hollow_C_2_2","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"L12_100":["hollow_C_1_1","hollow_C_1_2","hollow_C_2","ontop_CO_1","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"L12_110":["hollow_C_1_1","hollow_C_1_2","hollow_C_2","ontop_CO_1","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"L12_100_MAG":["hollow_C_1_1","hollow_C_1_2","hollow_C_2","ontop_CO_1","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"L12_110_MAG":["hollow_C_1_1","hollow_C_1_2","hollow_C_2","ontop_CO_1","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"B2_100":["hollow_C_1","hollow_C_2","ontop_CO_1","ontop_CO_2","slab_1","slab_2"]}
#set_dict={"B2_100_MAG":["hollow_C_1","hollow_C_2","ontop_CO_1","ontop_CO_2","slab_1","slab_2"]}
#set_dict={"B2_110":["hollow_C_1_1","hollow_C_1_2","ontop_CO_1_1","ontop_CO_1_2","slab_1"]}
#set_dict={"B2_110_MAG":["hollow_C_1_1","hollow_C_1_2","ontop_CO_1_1","ontop_CO_1_2","slab_1"]}
#set_dict={"L10_100":["hollow_C_1","hollow_C_2","ontop_CO_1","ontop_CO_2","slab_1","slab_2"]}
#set_dict={"L10_100_MAG":["hollow_C_1","hollow_C_2","ontop_CO_1","ontop_CO_2","slab_1","slab_2"]}
#set_dict={"L10_110":["hollow_C_1_1","hollow_C_1_2","ontop_CO_1_1","ontop_CO_1_2","slab_1"]}
#set_dict={"L10_110_MAG":["hollow_C_1_1","hollow_C_1_2","ontop_CO_1_1","ontop_CO_1_2","slab_1"]}
#set_dict={"FCC_100":["hollow_C_1","ontop_CO_1","slab_1"]}
#set_dict={"FCC_100_MAG":["hollow_C_1","ontop_CO_1","slab_1"]}
#set_dict={"BCC_100_MAG":["hollow_C_1","ontop_CO_1","slab_1"]}
#set_dict={"BCC_100":["hollow_C_1","ontop_CO_1","slab_1"]}
#set_dict={"L21_100":["hollow_C_1_1","hollow_C_1_2","hollow_C_2","ontop_CO_1","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"L21_110":["hollow_C_1_1","hollow_C_1_2","hollow_C_1_3","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_1_3","slab_1"]}
#set_dict={"L21_100_MAG":["hollow_C_1_1","hollow_C_1_2","hollow_C_2","ontop_CO_1","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"L21_110_MAG":["hollow_C_1_1","hollow_C_1_2","hollow_C_1_3","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_1_3","slab_1"]}
#set_dict={"XA_100":["hollow_C_1_1","hollow_C_1_2","hollow_C_2_1","hollow_C_2_2","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"XA_110":["hollow_C_1_1","hollow_C_1_2","hollow_C_1_3","hollow_C_1_4","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_1_3","ontop_CO_1_4","slab_1"]}
#set_dict={"D03_100":["hollow_C_1_1","hollow_C_1_2","hollow_C_2","ontop_CO_1","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"D03_110":["hollow_C_1_1","hollow_C_1_2","hollow_C_1_3","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_1_3","slab_1"]}
#set_dict={"D03_100_MAG":["hollow_C_1_1","hollow_C_1_2","hollow_C_2","ontop_CO_1","ontop_CO_2_1","ontop_CO_2_2","slab_1","slab_2"]}
#set_dict={"D03_110_MAG":["hollow_C_1_1","hollow_C_1_2","hollow_C_1_3","ontop_CO_1_1","ontop_CO_1_2","ontop_CO_1_3","slab_1"]}
sub_files=set_dict[list(set_dict.keys())[0]]
#print(set_dict.keys())
output_file={}
false_file=[]
ifile=0
isuc_ifile=0
nscf_limit=99
#for fname in glob.glob('./{0}/SLAB_*'.format(list(set_dict.keys())[0])):
for fname in glob.glob('./{0}/*_NOMAG'.format(list(set_dict.keys())[0])):
#for fname in glob.glob('./{0}/*_MAG'.format(list(set_dict.keys())[0])):
#for fname in glob.glob('./L12_110/SLAB_*'):
	ifile=ifile+1
	print(ifile)
	output_file_sub=[]
	for sfile in sub_files:
		print(fname+"/"+sfile)
		for outfiles in glob.glob(fname+"/"+sfile+"/output.*"):
			#print(os.path.isfile(outfiles+"/0/1/stdout.1.0"))
			if os.path.isfile(outfiles+"/0/1/stdout.1.0") == False :
				print("!================WARNING=======================!") 
				print("                       ")
				false_file.append(outfiles)
			#print(len(outfiles))
			#	print("CHECK")
			#print(outfiles)
			#print(len(outfiles))
			#if len(outfiles) != 1:
			#print(outfiles)
			if os.path.isfile(outfiles+"/0/1/stdout.1.0") == True :
				int_st,out_dict=qe_parameter_result_output.main_out_parameter_result_read(outfiles,outfiles+"/0/1/stdout.1.0")
				nscf=out_dict["RESULT_DATA"]["Times_converged_SCF"]
				n_it_scf=out_dict["RESULT_DATA"]["iterations_SCF"]
				job_done=out_dict["RESULT_DATA"]["JOB_DONE"]
				
				if out_dict["RESULT_DATA"]["JOB_DONE"] == True and nscf < nscf_limit and 200>n_it_scf > 0 and job_done==True:
					print("CAL SUCSESS")
					out_dict.update({"ABSITE_TYPE":sfile})
					output_file_sub.append(out_dict)
					
				else:
					print("!================CAL FALSE=======================!")
					print("         ")
					print("         ")
					false_file.append(outfiles)
		output_file.update({fname:output_file_sub})

				
			
print(len(output_file))
for f in false_file:
	print(f)

with open('output_sucsess.json', 'w') as f:
	json.dump(output_file,f, indent=4)
