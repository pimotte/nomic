
# Profiles

Profiles are meant to describe the play style of the player. Players can
increase or decrease their stats by playing the game.

Currently, there are no rules how to modify these stats, and they are
effectively frozen. 

The stats are bound to specific gameplay elements. The table below gives an
overview of their relation.

 1. (von) Karma is a Phoenix Wright reference and should reflect perfection in
 play. For instance, getting a proposal accepted without additions or
 retractions could increase this statistic.
 1. Afternoon Naps should reflect activity. An implementation could be the
 inactivity-streak: the number of consecutive days that a player has had no
 visible activity on GitHub.
 1. Heart Rate should reflect the number of times you (don't) get what you want.
 For instance, getting a proposal accepted lowers your heart rate, but being
 found guilty increases your heart rate.
 1. Hamsters show your supportive role in the game. You could obtain more
 hamsters by voting and making constructive comments on a proposal.

|            | (von) Karma | Afternoon Naps | Heart Rate | Hamsters |
| ---------- | ----------- | -------------- | ---------- | -------- |
| Proposals  |           x |              x |          x |          |
| Discussion |             |              x |            |        x |
| Voting     |             |              x |            |        x |
| Legal      |             |              x |          x |          |

