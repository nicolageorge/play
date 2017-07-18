while(i < n){
        numTransmitters++;

	/* Key is to use greedy algorithm to always place the transmitter at the house furthest to the right possible
	 * to cover the range.
	 */
        loc = x[i] + k; //let this i be i_orig
        //go to right as far as we cover i_orig as well.
        while(i < n && x[i] <= loc)
            i++;

        i--;    //this is where we place the transmitter
	cout << x[i] << " ";

	//now go to the right of x[i] by k because transmitter at x[i] covers houses to its right as well.
        loc = x[i] + k;
        while(i < n && x[i] <= loc)
            i++;
    }
