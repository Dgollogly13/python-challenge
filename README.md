# Python Challenge

The goal of this challenge was to analyze two sets of data and present the results in a concise and comprehensible fashion. The datatsets included polling results from four candidates in a local election and month to month profit or loss results for a financial institution. 

## Getting Started 

I am running this code out of my anaconda environment with Visual Studio Code and Jupyter Notebook. For running this code on your machine, you will need either of those applications with the proper dependencies installed or an equivalent such as PyCharm. 

### Analysis and Coding 

When analyzing the financial institution data, I utilized Python to loop through the dataset and produce the output displayed below:

```
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
   
    f"Total Months: {month_count}\n"
    f"Total: {total_net_value}\n"
    f"Average  Change: {net_change}\n"
    f"Greatest Increase in Profits: {greatest_gain}\n"
    f"Greatest Decrease in Profits: {greatest_loss}\n"
   )
```

I tackled the polling results with the pandas python library. By using various pandas functions I produced the voting results, including the election winner, as shown below:

```
voting_results_df = pd.DataFrame({"Khan": [2218231, '63%'],
                                  "Correy": [704200, '20%'],
                                  "Li": [492940, '14%'],
                                  "O'Tooley": [105630, '3%'],
                                  "Total Votes": [3521001, '100%'],
                                  "-": ["-", "-"],
                                  "Winner": ['Khan', winner_votes]
                                  })

final_df = voting_results_df.rename(index = {0: "Votes", 1: "Percent"})
final_df
```

### Challenges faced

One of the challenges I faced was displaying the data in the correct format, especially when using the Pandas library. Pandas is an amazing library for data analysis and the optimized functions allow for specific data summaries at speed, but I had to use quite a bit of hardcode when displaying the final dataframe. 

### Built With

* Python
* Pandas 

### Authors

* **Dallas Gollogly** - [dgollogly13](https://github.com/dgollogly13)

### Acknowledgments

* Denver University Data Analytics Bootcamp 
