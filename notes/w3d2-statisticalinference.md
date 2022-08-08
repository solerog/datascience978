<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 11 - Decision Science - Statistical Inference

## Goal of the week

How to increase the customer satisfaction.

## Probability refresher

Bayes
Random variable
Random process
Probability distribution
Normal distribution
Central Limit Theorem (CTL)
$p(X) = p(\mu,\sigma) \rightarrow p(\bar X) = p(\mu,s = \dfrac{\sigma}{\sqrt{n}})$
z-score $z = \dfrac{x - \mu}{\sigma}$

## Random sampling

Randomly select a `sample` of size $n = 1000$.

## Most Likelihood Estimate (MLE)

Most plausible value for a set of samples.

We have 95% of `confidence` that the mean $\mu$ will be between $\mu \plusmn 2\sigma$

## CDF

Calculates the area from the point to the left.
If we need the probability to the right we have to subtract the value to 1.
Or if we need to sum both parts we can multiply by 2.

## PPF

Used to calculate confidence interval

## Sample size considerations

`n` is considered _large enough_ if:

- `n` > 30
- `n` > 10 if observations are not skewed and without outliers

`n` is small enough if:

- `n` $<10%N$

## Experiment Design

1. Develop the feature
2. Create two groups (`control group` and `treatment group`)

## Null hypothesis

The original statement.
In this case:

- $H_o$: DARK mode changes nothing.
- $H_a$: Dark mode is better
- $\alpha = 0.05$: Significance level

We fail to reject the null hypothesis.

$P(\bar X | H_o) = $

$p-value$ = Probability of having a value with equal or lower probability.

## Power

_Power_ is the probability to correctly reject the null hypothesis.
The hgher the amount of samples `n`, the higher the _power_.

## z-score

How many times the value deviates from the mean

## t-tests

$$Z = \dfrac{\bar X - \mu}{\dfrac{\sigma}{\sqrt{n}}}$$
$$T = \dfrac{\bar X - \mu}{\dfrac{s}{\sqrt{n}}}$$

- Use `t-tests` instead of `z-tests`.
- Compute `confidence intervals` using `cdf`.
- Test hypothesis. Compute `p_value` with a significance level $\alpha$

## t-distribution

Degree of freedom. It is substracted to the sample value $n$.
Increasing the degree of freedom reduces the standard deviation.
One degree of freedom per column.
$T = \left(\dfrac{\bar X - \mu}{s/\sqrt{n}}\right)$

## Prior beliefs $p(H)$

If we don't have a prior belief, we can assume that all values have the same probability.

If we have a **prior belief**, we can update the belief as experiments are done using _Bayes_.
