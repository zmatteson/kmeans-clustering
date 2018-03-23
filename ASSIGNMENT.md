Instructions
For this assignment, you are implementing the k-Means clustering algorithm. The command to run the algorithm should be as follows:

./yourprog values.txt k

where values.txt is a space-separated file which contains a set of 2D objects with numeric attributes and k is the number of clusters you wish to find.

For example:


values.txt


12 32
43 25
178 234
32 49
156 200
 

values-output.txt

12 32 0
43 25 0
178 234 1
32 49 0
156 200 1

The output should be a space separated text file with the third column having the discovered cluster index for each data object. There should be no output to console.

To check your results and generate test data, you can visit dmlab.cs.txstate.edu/clusteringdemos/ where I've implemented k-Means as a simple browser program. You can click in the center field to generate points in the text area on the right side of the page. You can also cluster directly on this page and visualize the results, and you can copy your data that uses cluster indexing with integers (no clusters called 'a' or 'b' etc.) and visualize the clustering results.

For this assignment, please submit a report describing your implementation and include some test runs along with plots of your results. Combine these files into yournetid.zip. You are free to use whatever apparatus you want to make the plots, and this includes taking a screenshot of the clustering demo described previously.

Please do not import a library which already has k-Means implemented. This has happened in the past by students using scikit.learn and finding the k-Means implementation in there. The objective of this assignment is to get practice on the machinery of k-Means and have some programming practice in the process; not to analyze data.

There are two extra credit opportunities here:
1. Turn it in a week early for 5 extra points.
2. Cluster data with an arbitrary amount of dimensions without requiring any modification to the spec above. That is: the program is still called using the above command, and no additional parameters are added. If you have done this, say so in the report and show me some examples. This is also worth 5 extra points.