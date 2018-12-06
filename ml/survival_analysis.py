# Survival analysis is concerned with predicting the lifetime of something -- this could be actual lifetimes or
# something less morbid such as how long someone will stay subscribed to something


# Censorship:
# Let's take an example of when people will stop listening to a radio station. It is possible, likely TRUE, that
# your 'death' event hasn't happened yet in your data set. This makes more sense for an actual death -- someone
# probably won't wait until everyone in their data dies before starting their study (?)
# People who haven't died (or switched off the radio, or unsubscribed etc.) are RIGHT-CENSORED. We don't know what their
# behavior is after what we've observed.
# We can also have left-censorship, where we don't see when someone is born / switches on.

# Survival analysis, particularly Kaplan-Meier estimator is good with data that has "particularly right-censoring,
# which occurs if a patient withdraws from a study, is lost to follow-up, or is alive without event occurrence at last
# follow-up" - Wikipedia: https://en.wikipedia.org/wiki/Kaplan–Meier_estimator

from lifelines.plotting import plot_lifetimes
from numpy.random import uniform, exponential
import numpy as np
import matplotlib.pyplot as plt

N = 25 # Number of people we are looking at?
current_time = 10
actual_lifetimes = np.array([[exponential(12), exponential(2)][uniform() < 0.5] for i in range(N)])
observed_lifetimes = np.minimum(actual_lifetimes, current_time)
observed = actual_lifetimes < current_time

plt.xlim(0, 25)
plt.vlines(10, 0, 30, lw=2, linestyles='--')
plt.xlabel("time")
plt.title("Births and deaths of our population, at $t=10$")
plot_lifetimes(observed_lifetimes, event_observed=observed)
print("Observed lifetimes at time %d:\n" % (current_time), observed_lifetimes)

# Red lines are people we know about, blue are right-censored people. If we ignored the right-censored people, we'd
# be underestimating the average lifespan of the population.

# If we took the mean of what we have we'd still be underestimating, because we don't know what is going on with these
# right censored people. Maybe they live a lot longer than our cut-off!

# Case in point:
plt.xlim(0,25)
plt.vlines(10, 0, 30, lw=2, linestyles='--')
plot_lifetimes(actual_lifetimes, event_observed=observed)


# From lifelines: https://lifelines.readthedocs.io/en/latest/Survival%20Analysis%20intro.html
# "Survival analysis was originally developed to solve this type of problem, that is, to deal with estimation when our
# data is right-censored. Even in the case where all events have been observed, i.e. no censorship, survival analysis is
# still a very useful tool to understand durations.
# The observations need not always start at zero, either. This was done only for understanding in the above example.
# Consider the example where a customer entering a store is a birth: a customer can enter at any time, and not necessarily
# at time zero. In survival analysis, durations are relative: individuals may start at different times. (We actually only
# need the duration of the observation, and not the necessarily the start and end time.)"

# Let's estimate lifespan of regimes of leaders around the world!
# This is a cool dataset because censorship events would be those times when a leader died before their regime finished
# We use a Kaplan-Meier estimator or a product limit estimator. Non-parametric statistic to estimate survival from
# lifetime data.
import pandas as pd
from lifelines.datasets import load_dd

data = load_dd()
data.sample(2)
# the boolean columns `observed` refers to whether the death (leaving office)
# was observed or not.

# 'Observed' then tells us whether or not something is right-censored?

# For this example we'll use KaplanMeier but you can also use BreslowFlemingHarringtonFitter, WeibullFitter or
# ExponentialFitter
from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()

# "For this estimation, we need the duration each leader was/has been in office, and whether or not
# they were observed to have left office (leaders who died in office or were in office in 2008, the latest date this
# data was record at, do not have observed death events)"

# How the KaplanMeierFitter works:
#
# KaplanMeierFitter.fit(durations, event_observed=None,
#                       timeline=None, entry=None, label='KM_estimate',
#                       alpha=None, left_censorship=False, ci_labels=None)
#
# Parameters:
#   duration: an array, or pd.Series, of length n -- duration subject was observed for
#   timeline: return the best estimate at the values in timelines (postively increasing)
#   event_observed: an array, or pd.Series, of length n -- True if the the death was observed, False if the event
#      was lost (right-censored). Defaults all True if event_observed==None
#   entry: an array, or pd.Series, of length n -- relative time when a subject entered the study. This is
#      useful for left-truncated (not left-censored) observations. If None, all members of the population
#      were born at time 0.
#   label: a string to name the column of the estimate.
#   alpha: the alpha value in the confidence intervals. Overrides the initializing
#      alpha for this call to fit only.
#   left_censorship: True if durations and event_observed refer to left censorship events. Default False
#   ci_labels: add custom column names to the generated confidence intervals
#         as a length-2 list: [<lower-bound name>, <upper-bound name>]. Default: <label>_lower_<alpha>
#
#
# Returns:
#   a modified self, with new properties like 'survival_function_'.


# Fit our model
T = data["duration"]
E = data["observed"]

kmf.fit(T, event_observed=E)

# Has a built in command to look at survival function
kmf.survival_function_.plot()
plt.title('Survival function of political regimes');

# Y-axis means probability leader is still around after t years (t years is X-axis). So the more years, the less
# likely a leader will be around.

# Let's see how certain we can be about these predictions:
kmf.plot()

# Median time in office -- median duration of our observations
kmf.median_

ax = plt.subplot(111)

dem = (data["democracy"] == "Democracy")
kmf.fit(T[dem], event_observed=E[dem], label="Democratic Regimes")
kmf.plot(ax=ax, ci_force_lines=True)
kmf.fit(T[~dem], event_observed=E[~dem], label="Non-democratic Regimes")
kmf.plot(ax=ax, ci_force_lines=True)
plt.ylim(0, 1);
plt.title("Lifespans of different global regimes");

# We might be interested in estimating the probabilities in between some points. We can do that with the timeline argument.
# We specify the times we are interested in and are returned a DataFrame with the probabilities of survival at those points:
t = np.linspace(0, 50, 51)
kmf.fit(T[dem], event_observed=E[dem], timeline=t, label="Democratic Regimes")
ax = kmf.plot(ax=ax)
print("Median survival time of democratic:", kmf.median_)

kmf.fit(T[~dem], event_observed=E[~dem], timeline=t, label="Non-democratic Regimes")
ax = kmf.plot(ax=ax)
print("Median survival time of non-democratic:", kmf.median_)

# We can tell quite a bit just from graphs (non-democratic regimes last longer than democratic ones do)
# "Below we demonstrate this routine. The function logrank_test is a common statistical test in survival analysis
# that compares two event series’ generators. If the value returned exceeds some pre-specified value, then we rule that
# the series have different generators."
from lifelines.statistics import logrank_test

results = logrank_test(T[dem], T[~dem], E[dem], E[~dem], alpha=.99)

results.print_summary()

# Logrank is a "hypothesis test to compare the survival distributions of two samples. It is a non-parametric test and appropriate
# to use when the data are right-skewed and censored (techinally the censoring of the data should not be informative).
#  The test is also called a Mantel-Cox test. The logrank test statistic compares estimates of the hazard functions of the two
# groups at each observed event time. It's constructed by computing the observed and expected number of events in one of the
# groups at each observed event time and then adding these to obtain an overall summary across time points where there is an event.
# CENSORING MUST BE UNRELATED TO PROGNOSIS


# For data that is uncensored, you can use a Wilcoxon rank sum test."

# "The logrank test is based on the same assumptions as the Kaplan-Meier survival curve—namely, that censoring is
# unrelated to prognosis, the survival probabilities are the same for subjects recruited early and late in the study,
# and the events happened at the times specified. Deviations from these assumptions matter most if they are
# satisfied differently in the groups being compared, for example if censoring is more likely in one group than another."
# From Wikipedia: https://en.wikipedia.org/wiki/Logrank_test
 
