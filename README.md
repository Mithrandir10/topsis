# TOPSIS

Code by: Parteekpal Singh 

<hr style = "border:2px solid gray"> </hr>
## What is TOPSIS

TOPSIS stands for ‘The Technique for Order of Preference by Similarity to the Ideal Solution’ is a multi-criteria decision analysis(MCDA) method. It is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion.


## How to run

#### Before running, make sure you have pandas and numpy installed on your system

Open Terminal and input the following commands


>> pip3 install Topsis-Parteek-101803190



>> python
>>>from topsis.topsis import topsis
>>>topsis("input.csv","1,2,1,2","+,+,-,+","output.csv")

## Sample Input

This input was used to test the module

<table><thead><tr><th>Model</th><th>Corr</th><th>Rseq</th><th>RMSE</th><th>Accuracy</th></tr></thead><tbody><tr><td>M1</td><td>0.79</td><td>0.62</td><td>1.25</td><td>60.89</td></tr><tr><td>M2</td><td>0.66</td><td>0.44</td><td>2.89</td><td>63.07</td></tr><tr><td>M3</td><td>0.56</td><td>0.31</td><td>1.57</td><td>62.87</td></tr><tr><td>M4</td><td>0.82</td><td>0.67</td><td>2.68</td><td>70.19</td></tr><tr><td>M5</td><td>0.75</td><td>0.56</td><td>1.3</td><td>80.39</td></tr></tbody></table>

## Output 


<table><thead><tr><th>Model</th><th align="right">Corr</th><th align="center">Rseq</th><th>RMSE</th><th>Accuracy</th><th>Topsis Score</th><th>Rank</th></tr></thead><tbody><tr><td>M1</td><td align="right">0.79</td><td align="center">0.62</td><td>1.25</td><td>60.89</td><td>0.639133</td><td>2.0</td></tr><tr><td>M2</td><td align="right">0.66</td><td align="center">0.44</td><td>2.89</td><td>63.07</td><td>0.212592</td><td>5.0</td></tr><tr><td>M3</td><td align="right">0.56</td><td align="center">0.31</td><td>1.57</td><td>62.87</td><td>0.407846</td><td>4.0</td></tr><tr><td>M4</td><td align="right">0.82</td><td align="center">0.67</td><td>2.68</td><td>70.19</td><td>0.519153</td><td>3.0</td></tr><tr><td>M5</td><td align="right">0.75</td><td align="center">0.56</td><td>1.3</td><td>80.39</td><td>0.828267</td><td>1.0</td></tr></tbody></table>


## License

©️ 2020 Parteekpal Singh

This repository is licensed under the MIT license. See LICENSE for details.