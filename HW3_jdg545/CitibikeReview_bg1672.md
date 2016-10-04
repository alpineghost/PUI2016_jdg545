PUI2016, HW4
Author: Bailey Griswold
Citibike Review of jdg545

1. verify that their Null and alternative hypotheses are formulated correctly

JDGs idea is that there is higher city bike use during rush hour time because of commuting, so therefore the ratio of rides between peak times and non peak times on a weekday must be higher than that same ratio on a weekend day.  So, on weekends there would not be much difference in the number of rides at peak times and non peak times but on weekdays there would be.

His null hypothesis is stated correctly: \"The ratio of rush hour trips to non-rush hour trips on weekdays is the same or smaller than the ratio of rush hour trips to non-rush hour trips on weekends.
 I will use a significance level $\\alpha=0.05$\"

He did not, however, state the alternative hypothesis or give the formulas for either.  The alternative hypothesis should be:
The ratio of rush hour trips to non-rush hour trips on weekdays is greater than the ratio of rush-hour trips to non-rush hour trips on weekends.
$H_a = P_1 - P_0 > 0$
$H_0 = P_1 - P_0 <= 0$ 

To be more specific, he could have also stated the rush hour times in the hypothesis.

2. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test has not been chosen yet)

The variables JDG should look at are the start time and the start date.  He did a cool thing by pulling out rides that occurred in two windows (the am rush period and the pm rush period) and then put them into one dataframe.  Then he did the same thing for the non rush times.  Then he plotted them on a histogram together. A funny thing happened with his histogram: when one graph is plotted over the other, the colors combine to form a new color.  On the weekdays, the rush hour rides are greater than the non rush, so the non-rush rides look purple, with the red rush rides peaking over the top of the bars.  But the opposite happens on the weekend: the nonrush rides outnumber the rush rides, so instead of red peaking out the top of the overlapped graphs, it is blue.   Based on that histogram it seems like his origional idea is supported.  It looks like a big difference in rush to nonrush rides on the weekend and weekday.


3. Chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or to the CSU cheat-sheet here, of Statistics in a Nutshell.

The test that should be used should be a factorial ANOVA with two factors.  Using the flow chart from PUI Lecture 4, we can follow that this test uses ratios, we are looking at group differences, the observations are not paired, and there is more than independant variable (day of the week and time of day).  We use ANOVA because we want to know the effect of these independant variables on the dependant variable (the number of rides).  We use the ANOVA instead of the linear regression because the independent variables are not continuous: we have grouped day of the week into weekday and weekend, and we have grouped time of day into rush and non rush.

The questions asked is inferential: the analysis is attempting to determine a relationship between the variables, but it extends beyon mere exploratory because the statistical tests allow us to extrapolate the results of our sample to the population.  
