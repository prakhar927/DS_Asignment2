Problem Statement 

Given a list of the wealth of people, you are tocreate communities of max ssize such that they are formed by grouping people living next to each other. If in each community, every member becomesas  rich  as  it’s  richest  member,  you  need  to  find  what  can  be  the  maximum  total  wealthof  all communities put together.

For example:Consider the following input: 3::1 15 7 9 2 5 10

Where s = 3 and there are 7 people with individual wealth of 1 15 7 9 2 5 10 respectively. 

You can consider that the sequence of the 7people indicates who livesnext to whom. To maximize the total wealth of all the communities, the following communities need to be formed.

1 15 7 | 9 |2 5 10(remember  that  maximum  community  size  can  be  s(3)  and  only  people  living together  can  form communities)Now every member of a community becomes as rich as it’s richest member: 15 15 15 | 9 | 10 10 10

So maximum total wealth possible is 15 + 15 + 15 + 9 + 10 + 10 + 10 = 84

For a given set of individuals, and specifiedcommunitysize, you are required to find the maximum total wealth possiblefor each of the inputs. 
