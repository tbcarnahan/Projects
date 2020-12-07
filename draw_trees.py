# -*- coding: utf-8 -*-                                                         
print '------> Setting Environment'

import sys
import math
from ROOT import *
import numpy as np
from array import *
from termcolor import colored
from ROOT import gROOT
## run quiet mode                                                              \
                                                                                
sys.argv.append( '-b' )
gROOT.SetBatch(1)

print '------> Importing Root File'

## ================ Read input files =============                              
dir1 = '/uscms/home/carnahan/nobackup/CMSSW_11_2_0_pre7/src/'
file_name = dir1+"step1.root"
print colored('Loading file: '+file_name, 'green')

## ============== Read in the tree ================                             
evt_tree = TChain('Events')
evt_tree.Add(file_name)

## ============== Plotting macro ==================
#Print out the list of all leaves in the TTree for b in evt_tree.GetListOfBranches():                                                                          

#for b in evt_tree.GetListOfBranches():                                         
#  c1 = TCanvas("c1")                                                           
#  evt_tree.Draw(b.GetName())                                                   
#  c1.SaveAs('plots/'+b.GetName()+'.png')                                       
#  print ("branch:",b.GetName())                                                
#  c1.Close()                                                                   

#If you want to draw a single leaf, for example the true muon pT:               

#update from Dec 1st to draw single leaves for eta and pt; make sure to '!!!!!                       

c1 = TCanvas("c1")
evt_tree.SetAlias("pt()", "recoGenParticles_genParticles__SIM./recoGenParticles_genParticles__SIM.obj")
evt_tree.Draw("pt()")
c1.SaveAs('plots/gen_pt.png')

#c1 = TCanvas("c1")                                                             
#evt_tree.Draw("eta()")                                                         
#c1.SaveAs('plots/eta().png')  #Save your plot into a folder named 'plots' (mkdir this folder first)                                                           


#You can apply simple selections to whatever you plot. The selection is the second argument in tree.Draw()                                                     
#Our muons go up to 1000 GeV, but let's try only plotting up to 100 GeV         
#c1 = TCanvas("c1")                                                             
#evt_tree.Draw("mu_pt", "(mu_pt < 100)")                                        
#raw_input("Press Enter to continue")                                           

#Or plot the distribution of eta for true muons less than 10 GeV                
#c1 = TCanvas("c1")                                                             
#evt_tree.Draw("mu_eta", "abs(mu_eta)>1.2")                                     
#raw_input("Press Enter to continue")                                           

#Or the distribution of hit_eta for CSC hits in ME1/1;                          
#Good for correlation plots evt_tree.Draw("var1:var2","selection")              
#c1 = TCanvas("c1")                                                             
#evt_tree.Draw("hit_eta", "(hit_isCSC==1 && hit_station==1 && hit_ring==1)")    
#raw_input("Press Enter to continue")                                           


#If you wanted to draw and save -every- leaf in the tree:                       
#Note that this might not be a good idea if you want to apply selections to certain plots.                                                                     

#for b in evt_tree.GetListOfBranches():                                         
 # c1 = TCanvas("c1")                                                           
 # evt_tree.Draw(b.GetName())                                                   
 # c1.SaveAs('plots/'+b.GetName()+'.png')                                       


#If you don't like the default draw options (title, x-title, y-title,...)       
#Here is a way to adjust them. There isn't a simple option to do this, but you can define a 'dummy' histogram over your canvas that has a different title or axes.                                                                            
# c1 = TCanvas("c1")                                                            
# evt_tree.Draw("mu_pt")                                                        
# htemp = gPad.GetPrimitive("htemp")                                            
# htemp.SetTitle("Generated muon p_{T}") #Plot title                            
# htemp.GetXaxis().SetTitle("p_{T} (GeV)") #X-axis title, can do same for y-axis                                                                               
# gPad.Update()               
# raw_input("Press Enter to continue")
