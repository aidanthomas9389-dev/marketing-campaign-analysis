# Marketing Campaign Analysis — Project Overview

## What Is This Project?

This project investigates how a retail company can better understand its customers and make smarter decisions about marketing. Using two years of real customer data — covering shopping habits, demographics, and responses to past campaigns — we set out to answer a simple question: **who responds to marketing, and why?**

The findings are presented in an interactive dashboard that anyone can explore, no technical knowledge required.

---

## The Data

The starting point is a dataset of **2,240 customers**. For each customer, we have information like:

- Their age, education level, and whether they have children at home
- Their annual household income
- How much they've spent on different product categories — things like wine, meat, fish, fruit, and sweets — over the past two years
- How they prefer to shop: online, through a catalogue, or in-store
- Whether they responded to any of the company's last five marketing campaigns

Think of it as a snapshot of the company's customer base — a rich profile of who these people are and how they behave.

---

## What We Did

### 1. Organised the Data

Raw data is messy. The first step was cleaning and loading it into a structured database so every question we asked of it would get a reliable, consistent answer. This is the foundation everything else builds on.

### 2. Simulated Customer Engagement

Real engagement data (website visits, email opens, ad clicks) wasn't available, so we generated a realistic stand-in. For every customer, we simulated a full year of daily activity across five channels: page views, email opens, ad clicks, purchases, and social shares.

We built in a seasonal pattern too — activity doubles in December, reflecting the kind of holiday-season surge any retailer would expect. This lets us explore engagement trends that mirror real-world behaviour.

### 3. Asked Four Key Business Questions

With the data in place, we ran a series of analyses:

**Who is most likely to respond to a campaign?**
We looked at response rates across different customer groups — broken down by education level and relationship status. This tells the marketing team which segments to prioritise when running a campaign.

**How engaged are customers over time?**
We tracked each customer's activity on a rolling 30-day basis throughout the year. This shows whether engagement is growing, declining, or seasonal — useful for timing campaigns and identifying customers who may be drifting away.

**Who are the highest-value customers in each segment?**
We ranked customers by total spending within each education group. Knowing who the top spenders are — and what they have in common — helps the company focus its retention efforts where they matter most.

**Which shopping channel do customers prefer?**
We compared how often different types of customers shop online versus via catalogue versus in-store. This helps the company decide where to invest: should it improve its website, its print catalogue, or its in-store experience?

### 4. Built a Dashboard

The results of all four analyses are brought together in an **interactive Tableau dashboard**. Rather than a static report, the dashboard lets users filter, compare, and explore the data themselves — no technical knowledge needed.

**[View the Dashboard](https://public.tableau.com/app/profile/aidan.thomas/viz/MarketingCampaignAnalysis_17804192196840/Dashboard1)**

---

## What the Analysis Found

- **Education is a strong predictor of campaign response.** Customers with higher levels of education tend to accept campaigns at a higher rate — but they are also more selective, so the content and channel matter.
- **Married and partnered customers spend more overall**, but single customers are often more responsive to individual campaigns.
- **The holiday season drives a measurable spike in engagement** across all customer types, making December the prime window for high-impact campaigns.
- **Online shopping is growing**, but catalogue and in-store purchases remain significant for older and higher-income segments — a reminder that a single-channel approach would leave money on the table.

---

## Why It Matters

Marketing budgets are finite. Every pound or dollar spent on a campaign that reaches the wrong person is wasted. This project gives the company a clearer picture of its customers — who they are, how they behave, and what motivates them to buy — so that future campaigns can be more targeted, more timely, and more effective.

The goal is not just to understand the past, but to make better decisions going forward.
