/*
Task: Modify the PtRegressionPrepRun3.C in order to declare histograms and dump information into them;
more specifically, develop code to see what a variable is doing and how it behaves
Show how SLOPE is behaving in each endcap

Reference: https://root.cern/doc/master/hsum_8C.html 
*/

std::cout << "Preparing Histograms" << std::endl;

//Inside PtRegressionRun3Prep.C

void h_slope() {
	TCanvas *c1 = new TCanvas("c1", "Slope vs +endcap",200,10,600,400);
	c1->SetGrid(); //why called c1; can I call it anything?

	gBenchmark->Start("h_slope");

	//Create some histograms. (Reference: https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html)

	auto slope = new TH2F("slope v endcap", "Slope v. Endcap", 100, -10, 10, 100, -10, 10) //do total range for endcaps here
	//TH1F--(what you call it, title of graph, (bins?), range of x)
	//TH2F--(name, title, x dim (100, -10, 10), y dim (100, -10, 10))--when add dimensionality, need to add dimensionality
	slope->SetMarkerStyle(21);
	slope->SetMarkerSize(0.7);
	slope->SetFillColor(14); //can use any parameter to help define histo

	//Fill histogram

	slope->Fill(endcap,slope_1); //with variables? Since it's TH1f, can Fill(x); if TH2F Fill(x,y)
	slope->Fill(endcap, slope_2);
	slope->Fill(endcap, slope_3);
	slope->Fill(endcap, slope_4); //correct syntax for trying to fill with variables? Need {}?

	c1->Update();
	slope->Draw();
	gBenchmark->Show("h_slope");

	

}