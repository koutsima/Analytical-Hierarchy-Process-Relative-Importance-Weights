# Analytical-Hierarchy-Process-Relative-Importance-Weights

I've created this very simple piece of code to obtain relative importance weights (RIW) for Multi-criteria Analysis' criteria, using Saaty's Analytical Hierarchy Process (AHP). Number of criteria must be between 3 and 10. 

The user inputs: 

1) number of criteria, 
2) criteria names and 
3) their preference for one criterion over another by executing pairwise comparisons between the criteria, using Saaty's scale. 

The program prints out the comparison matrix, its eigenvector and the maximum eigenvalue. The maximum eigenvalue is computed using two approaches. The value of the second approach is used in the computation of the Consistency Index (CI). Values for the Random Index (RI) are taken from the literature. 
The program finally checks whether the Consistency Ratio (CR) is acceptable or not. If it is, then the user is informed about the relative imprtance weights of the criteria. If it's not, then they should reconsider their preferences.
