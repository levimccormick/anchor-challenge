# anchor-challenge
A small program to complete a challenge laid out in a job listing for Anchor.fm.

While looking into Anchor as a podcast platform, I found a job posting for a
Server & API engineer. It had a clever little programming challenge in it. I
decided to solve it.


> https://boards.greenhouse.io/anchor/jobs/4001832002
>If you want to jumpstart the process of talking to us about this role, here’s a little challenge: write a program that outputs the largest unique set of characters that can be removed from this paragraph without letting its length drop below 50. For example: [‘H’, ‘i’, ‘!’, ‘ ’]

For a more robust solution, I should add a unit test. I'd use pytest to verify
that the resulting text would be greater than 50 characters. I provided a Docker file because I do all my work in Docker now.
