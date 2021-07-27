/*
Task: Modify the PtRegressionPrepRun3.C in order to declare histograms and dump information into them;
more specifically, develop code to see what a variable is doing and how it behaves
Show how SLOPE is behaving in each endcap
*/

std::cout << "Preparing Histograms" << std::endl;

//Inside PtRegressionRun3Prep.C

//Initialize histograms (need 2D?) and realize the difference between slope and bend

if (endcap > 0)
{
	h_slope_endcap_pos = TH2D('h_slope_endcap_pos', 'Slope v endcap +1', 25, 0, 10, 25, 0, 10);//name,title,nbinsx,xlow,xup,nbinsy,ylow,yup
		//TH1D contains one double per bin = more precise
	h_bend_endcap_pos = TH2D('h_bend_endcap_pos', 'Bend v endcap +1', 25, 0, 10, 25, 0, 10); //see a distinction between slope and bend v endcap
	
	std::cout << "You are in the positive endcap region.\n";

	//Dump data; Fill()--need ALL slope variables associated

	h_slope_endcap_pos->Fill((endcap), (slope_1)); //(x),(y)? how do we designate the correct variables?
	h_slope_endcap_pos->Fill((endcap), (slope_2)); //// C++ '->' = Python's '.'
	h_slope_endcap_pos->Fill((endcap), (slope_3));
	h_slope_endcap_pos->Fill((endcap), (slope_4)); //can I make each slope variable associated with a defining color --maybe define in a legend later?

	h_bend_endcap_pos->Fill((endcap), (bend_1));
	h_bend_endcap_pos->Fill((endcap), (bend_2));
	h_bend_endcap_pos->Fill((endcap), (bend_3));
	h_bend_endcap_pos->Fill((endcap), (bend_4)); //can I make more succint? As in defining bend = bend_1, bend_2, etc...

	c1 = TCanvas('c1', '', 200, 10, 700, 500) //correct vertices?
	h_slope_endcap_pos->Draw()
	gStyle->SetOptStat(0)
	//gPad->SetLogz()
	h_slope_endcap_pos.SetTitle('slope vs + endcap')
	h_slope_endcap_pos->GetXaxis()->SetTitle('Endcap (eta range)') ; h_slope_endcap_pos->GetYaxis()->SetTitle('slope')
	h_slope_endcap_pos->Write()
	c1->SaveAs('asymmetry_Qs/h_slope_endcap_pos.png')
	c1->Close()

	c2 = TCanvas('c2', '', 200, 10, 700, 500)
	h_bend_endcap_pos->Draw()
	gStyle->SetOptStat(0)
	//gPad->SetLogz()
	h_bend_endcap_pos.SetTitle('bend vs + endcap')
	h_bend_endcap_pos->GetXaxis()->SetTitle('Endcap (eta range)') ; h_bend_endcap_pos->GetYaxis()->SetTitle('bend')
	h_bend_endcap_pos->Write()
	c1->SaveAs('asymmetry_Qs/h_bend_endcap_pos.png')
	c1->Close()




	else
		h_slope_endcap_neg = TH2D('h_slope_endcap_neg', 'Slope v endcap -1', 25, -10, 5, 25, -10, 0);
		h_bend_endcap_neg = TH1D('h_bend_endcap_neg', 'Bend v endcap -1', 25, -10, 5, 25, -10, 0);

		std::cout << "You are in the negative endcap region.\n";

		h_slope_endcap_neg->Fill((endcap), (slope_1));
		h_slope_endcap_neg->Fill((endcap), (slope_2));
		h_slope_endcap_neg->Fill((endcap), (slope_3));
		h_slope_endcap_neg->Fill((endcap), (slope_4)); //can I make each slope variable associated with a defining color --maybe define in a legend later?

		h_bend_endcap_neg->Fill((endcap), (bend_1));
		h_bend_endcap_neg->Fill((endcap), (bend_2));
		h_bend_endcap_neg->Fill((endcap), (bend_3));
		h_bend_endcap_neg->Fill((endcap), (bend_4));
return 0;
}

/*
Confused as to which route to go... the above or 2 frameworks below?
*/

//Using the declare histogram https://root.cern.ch/doc/master/classTH1.html#creating-histograms

TH2 *h2 = new TH2F("h2", "Slope vs. Endcap Ranges", 100, -10, 10, 100, -10, 10)
	//(h1, title;x-axis;y-axis;)

	//histograms can also be created by calling the Clone() function.

	//if want to find histogram, use TH1F *h1 = (TH1F*)gDirectory->FindObject(name);

//Want to fill histogram with a data dump

h2->Fill(endcap, slope_1); //(endcap) = (x)...how do we get more than 1 variable on y-axis?
	//h1->Fill(endcap,w); //fill with weight

//Draw histogram:

h2->DrawCopy(); //draws current version of histogram in a pad

//Saving/reading histograms to/from a ROOT file:

TFile f("histos.root", "new");
TH2F h2("h2", "Slope vs. Endcap Ranges", 100, -10, 10, 100, -10, 10);
h2->Fill("slope")
h2->Write();


//What's the difference between doing this the T-Canvas way? *Still don't know how to Fill below with the data dump
//using the below above now
/*

c1 = TCanvas('c1', '', 200, 10, 700, 500)
h_slope_endcap_pos->Draw()
gStyle->SetOptStat(0)
//gPad->SetLogz()
h_slope_endcap_pos.SetTitle('slope vs + endcap')
h_slope_endcap_pos->GetXaxis()->SetTitle('Endcap (eta range)') ; h_slope_endcap_pos->GetYaxis()->SetTitle('slope')
h_slope_endcap_pos->Write()
c1->SaveAs('asymmetry_Qs/h_slope_endcap_pos.png')
c1->Close()

*/