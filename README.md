Nomic: The GitHub Edition 
=========================

Nomic is a game wherein the point is to change the rules of the game. The
[original paper](http://www.earlham.edu/~peters/writing/nomic.htm) goes to great
depths explaining just why this is a fun and worthy use of time. Everyone should
at least make a stab at reading that. This file is in 
[GitHub-flavored Markdown](http://github.github.com/github-flavored-markdown/)

Player List 
-----------
1. [Pim Otte](players/pimotte.md) (@pimotte)
2. [Stefan Hugtenburg](players/mrhug.md) (@MrHug)
3. [Arthur Bik](players/arthurbik.md) (@arthurbik)
4. [Jesse Donkervliet](players/jdonkervliet.md) (@jdonkervliet)
5. [Otto Visser](players/maninthegithub.md) (@ManInTheGitHub)
6. [Pim Veldhuisen](players/pimveldhuisen.md) (@pimveldhuisen)

# Rules

## Immutable Rules 

**101** *Everyone needs a code they can live by*

All players must always abide by all the rules then in effect, in the
form in which they are then in effect. The rules in the Initial Set are in
effect whenever a game begins. The Initial Set consists of Rules 101-116
(immutable) and 201-214 (mutable).

**102** *Laying Down the Law* 

Initially rules in the 100's are immutable and rules in the 200's are
mutable. Rules subsequently enacted or transmuted (that is, changed from
immutable to mutable or vice versa) may be immutable or mutable regardless of
their numbers, and rules in the Initial Set may be transmuted regardless of
their numbers.

**110** *Constitution Trumps Law*

In a conflict between a mutable and an immutable rule, the immutable
rule takes precedence and the mutable rule shall be entirely void. For the
purposes of this rule a proposal to transmute an immutable rule does not
"conflict" with that immutable rule.

**116** *Chaos is Allowed*

Whatever is not prohibited or regulated by a rule is permitted and
unregulated, with the sole exception of changing the rules, which is permitted
only when a rule or set of rules explicitly or implicitly permits it.

## Mutable Rules

**209** *Conflict Resolution*

If two or more mutable rules conflict with one another, or if two or
more immutable rules conflict with one another, then the rule with the lowest
ordinal number takes precedence.

If at least one of the rules in conflict explicitly says of itself that it
defers to another rule (or type of rule) or takes precedence over another rule
(or type of rule), then such provisions shall supersede the numerical method for
determining precedence.

If two or more rules claim to take precedence over one another or to defer to
one another, then the numerical method again governs.

# Rule Changes

## Immutable Rules

**103** *Panta Rei* 

A rule-change is any of the following: (1) the enactment, repeal, or
amendment of a mutable rule; (2) the enactment, repeal, or amendment of an
amendment of a mutable rule; or (3) the transmutation of an immutable rule into
a mutable rule or vice versa.

(Note: This definition implies that, at least initially, all new rules are
mutable; immutable rules, as long as they are immutable, may not be amended or
repealed; mutable rules, as long as they are mutable, may be amended or
repealed; any rule of any status may be transmuted; no rule is absolutely immune
to change.)

**104** *Popularity Contest* 

All rule-changes proposed in the proper way shall be voted on. They will
be adopted if and only if they receive the required number of votes.

**106** *Speaking is Silver, Writing is Gold* 

All proposed rule-changes shall be written down before they are voted
on. If they are adopted, they shall guide play in the form in which they were
voted on.

**107** *Ex Post Facto Prohibition* 

No rule-change may take effect earlier than the moment of the completion
of the vote that adopted it, even if its wording explicitly states otherwise. No
rule-change may have retroactive application.

**108** *Numbering the World* 

Each proposed rule-change shall be given a number for reference. The
numbers shall begin with 301, and each rule-change proposed in the proper way
shall receive the next successive integer, whether or not the proposal is
adopted.

If a rule is repealed and reenacted, it receives the number of the proposal to
reenact it. If a rule is amended or transmuted, it receives the number of the
proposal to amend or transmute it. If an amendment is amended or repealed, the
entire rule of which it is a part receives the number of the proposal to amend
or repeal the amendment.

**109** *Constitutional Amendment* 

Rule-changes that transmute immutable rules into mutable rules may be
adopted if and only if the vote is unanimous among the eligible voters.
Transmutation shall not be implied, but must be stated explicitly in a proposal
to take effect.

**114** *Nothing is Set in Stone*

There must always be at least one mutable rule. The adoption of
rule-changes must never become completely impermissible.

**115** *Making Gödel Happy*

Rule-changes that affect rules needed to allow or apply rule-changes are
as permissible as other rule-changes. Even rule-changes that amend or repeal
their own authority are permissible. No rule-change or type of move is
impermissible solely on account of the self-reference or self-application of a
rule.

## Mutable Rules

**203** *Number of Required Ayes*

A rule-change is adopted if and only if at least a simple majority
of the players votes in favour of the rule-change.

**204** *Effective Immediately*

An adopted rule-change takes full effect at the moment of the completion
of the vote that adopted it.

**328** *Neat and Tidy*

All player scores will be tracked in separate files for each player. These files should contain at least the
following:
- The player's name.
- The player's GitHub handle.
- The current total score of the player.

Other items may be added to these player files through non-rule-change Pull Requests. Players are encouraged to keep a
list of Pull Requests that were merged and how many points this netted them, so that the total can be easily recomputed. 

The total score of the player must reflect the gamestate.

Players are excempt from this rule so long as they do not have at least one merged rule-change Pull Request. They can
temporarily record their initial score in the player list.

**309** *Pull, Don't Push*

A rule-change is proposed by submitting a pull request, such that
merging the pull request reflects the accurate state of the game after
adoption of the rule-change. In case the rule-change has been given a number
for reference, this number must be included in the title of the pull request.

**312** *Let's Call the Moving Men*

In addition to other types of valid rule-changes outlined in the rules, a rule-change may also consist of moving
a part of an existing mutable rule into a new mutable rule. In order for this rule-change to be valid, the phrasing of
the new rule must be identical to the phrasing of the clause or sentence in the old rule and the new rule must be
self-contained, meaning it does not require a reference to the old rule to be understood. Similarly the old rule must
still be self-contained and sensible with part of it removed.

# Non-Changes

## Mutable Rules

**319** *Sorry, No Change*

Both players and non-players are allowed to submit a pull request to master on pimotte/nomic, 
without this pull request containing any changes to any rule's text or the game state. 
With the single exception that rule's text may be changed 
if the change is the correction of spelling and/or grammar mistakes in mutable rules.
Such a pull request will be voted on as if they were a rule-change affecting only mutable rules. 
Such a pull request will be merged by someone with the power to do so, in a timely fashion, if
and only if the votes on the pull request are such that a rule-change with the same votes would
be adopted. If a pull request only adds the initiators name to, or removes the initiators
name from the player list, that pull request
will not be voted on. Instead, it may be merged by any person who has the right to do so.

**316** *What's in a name?* 

Rules may have a title.
If a rule has a title, the title must follow any rule number, preceed any of the rule's text and be 
formatted in *italic*.
If a rule has a title, the title must uniquely identify the rule.
The title of a rule is not part of the rule's text, but is encouraged to be related to the content
of the rule. 

# Voting

## Immutable Rules

**105** *Democracy*

Every player is an eligible voter. 

**111** *Room for Discussion*

Other players may suggest amendments or argue
against the proposal before the vote. A reasonable time must be allowed for this
debate. The proponent decides the final form in which the proposal is to be
voted on and, unless the Judge has been asked to do so, also decides the time to
end debate and vote.

## Mutable Rules

**205** *You've Got a Point*

When a proposed rule-change is adopted, the player who proposed it
gains 1 point.


**315** *Democracy Reloaded*

Each eligible voter always has exactly one vote.


**336** *Everyone, get in here!*

A PR should remain open for at least 24 hours, regardless of what other rules specify, before it can be merged, unless
unanimity in votes is achieved before this time.

This rule only applies to PRs that need to be voted on.


**349** *Thumbs Up!*

A player can vote in favor of a rule-change by commenting on the pull request
with a comment that consists only of ":+1:". Likewise, a player can vote against
a rule-change by commenting on the pull request with a comment that consists
only of ":-1:". 

A commit on a pull request dated after any votes voids those votes, 
unless this commit is a merge commit resulting from a merge from master on pimotte/nomic to 
the source branch of the pull request and does not alter the proposed rule-change, or unless
the commit only fulfills a condition from a conditional vote, in which case any conditional
votes including that condition will not be voided.

If the rule-change is adopted, a player who can shall merge the pull request
in a timely fashion, unless another rule specifies to wait.
The merging of the pull request marks completion of the vote.

**367** *Warning, no dawdling*

During a simple majority vote, a player may warn the other players that the vote is going to end.
If this warning raises no objections and a reasonable time has passed, the vote ends and the rule
is adopted when a majority of the votes that are cast are in favor of the rule-change. 
A reasonable time in this context is at least 72 hours and is at least enough time for the warning
to reach all other players and for all other players to react to the warning. 
An objection can be raised by any player at any time, this includes the option to raise objections
to future warnings. Commits that invalidate votes, also invalidate warnings. 
Warnings on a PR that has a dependency automatically implies a warning on that dependency.


**321** *Retraction Watch*

A vote can be retracted by commenting on the pull request with a comment that 
consists only of ":wave:". This will retract any votes made by the player that were made before
this comment. A vote can only be retracted as long as it is valid and the rule-change is not
yet adopted or rejected.

**323** *The Couple will not Object to Their Own Wedding*

It may be assumed that the proposer of a rule-change is always in favour of this rule-change and thus has
cast an implicit vote in favour of the rule-change. 
An explicit vote through the procedures outlined in the rules replaces this implicit vote in favour.
If the implicit vote is not overwritten with an explicit vote, the validity of the implicit vote is held to the same
requirements as any other vote. For the purpose of validity checking, it can be considered an unwritten comment placed
after all comments on the PR before the merging comment of the PR.

**330** *Conditional Voting*

A player may cast a conditional vote by posting a comment in the following format:

```
IF [condition] THEN [voting post] (ELSE [voting post])
```

In this format, items in between parentheses are optional. `[condition]` should
be replaced with a human readable condition. If this condition cannot be resolved
at a time when a player attempts to do so, for example because of improper formulation or
a logical paradox, it will be resolved as being false.

`[voting post]` should be replaced by the contents of a comment representing the vote,
or an empty string. Conditional votes are a comment representing a vote.

In order to perform an action based on resolution of one of more conditional votes,
a player must post a comment describing the resolution before performing said action.

**368** *Dependency Hell*

The owner of a PR may declare one dependency of this PR (henceforth "child") on another
PR (henceforth "parent"), by including the text
"This PR is dependent on #<number of parent>" in an unedited post. Any votes above
this post are voided. A child PR must be of a branch that branches off the
branch of the parent at the moment of declaring the dependency. Both PRs must be on master.

A vote in favour on a child implies a vote in favour on its parent. This vote shall be read
as a comment representing a vote in favour on the parent just before merging 
for the purposes of other rules.

A child may be formulated as if the parent is the current ruleset.

If a commit that invalidates votes is added on a parent, any vote that
implied one on that parent at that time is invalidated.

The player who submitted the parent may declare the dependency to be "strict". 
This is done by including the text "#<number of parent PR>'s dependency is strict" in an unedited post.
Any votes above this post are voided.

If a dependency is strict, the parent PR may not be merged seperately from the child.

It is not allowed to withdraw a dependency. If a parent is closed without being merged, the
child must also be closed without being merged.





# Win Condition & Participation

## Immutable Rules

**112** *You Win the Game!*

The state of affairs that constitutes winning may not be altered from
achieving n points to any other state of affairs. The magnitude of n and the
means of earning points may be changed, and rules that establish a winner when
play cannot continue may be enacted and (while they are mutable) be amended or
repealed.

**113** *Torture Prevention Measures*

A player always has the option to forfeit the game rather than continue
to play or incur a game penalty. No penalty worse than losing, in the judgment
of the player to incur it, may be imposed.

## Mutable Rules

**207** *Some Random Number*

The winner is the first player to achieve 200 (positive) points.

**211** *Don't Get Stuck!*

If the rules are changed so that further play is impossible, or if the
legality of a move cannot be determined with finality, or if by the Judge's best
reasoning, not overruled, a move appears equally legal and illegal, then the
player who proposed the last adopted rule wins.

This rule takes precedence over every other rule determining the winner.

**213** *Joining the Game*

A non-player can become a player by submitting a pull request which adds
their name and Github handle to the Player List.

**332** *The Trophy of Awesome*

Whenever a player wins the game a virtual "Trophy of Awesome"
will be created, inscribed with their name and the date on which they won.
A new game will be started, with the game state set to the latest point 
at which the win was not inevitable. 
To this game state the Trophy will be added. Furthermore,
if the win was achieved through obtaining a required number of points,
the points of the winner will be set to the average of the other
players rounded to the nearest integer.
In case of non-consensus about the reset point, the Trophy recipient
decides.

**331** *I'll be Back!*

A player may at any time create an issue stating they are on hiatus, with the
label "Hiatus". As long as this issue is open, this player will be considered
to be a non-player for all intents and purposes, including but not limited
to voting and jury selection. Players which currently play any role in a Trial
or are Judge in a Judgement may not perform this action.

**351** *So long, and thanks for all the fish*

If a player A doubts the activity of another player B and player B has not shown
any sign of activity for a period of at least 7 days on GitHub in pimotte/nomic, player A can
create an issue titled `Calling forth player X` where `X` is the GitHub handle of player B.

Player B then has 2 weeks to respond to this issue thus indicating he is still
wants to actively take part in the game. If he has not responded after 2 weeks,
player A may declare player B to be on hiatus.

This state of hiatus is automatically lifted when player B responds to the issue,
showing he is still alive and active. After this response the issue shall be closed.


# Turns

## Mutable Rules 

**303** *Everybody Gets All the Turns!*

A player may have an infinite number of concurrent turns.
A player may start a turn regardless of the state of their other turns.


**202** *Just the One?* 

One turn consists of proposing one rule-change and having it voted on.

# Points

## Mutable Rules

**325** *Starting from Square One?*

All players begin with the number of points equal to the outcome of this formula:
`max(0, min_i(#points of player i) - 2)`

**376** *Scrambling for points*

A **point-awardable condition** is a condition on a PR on master of pimotte/nomic
that may be rewarded with a number of points. 

PRs are only eligble for point-awardable conditions if they are to be voted on.

A rule implementing a point-awardable condition must at least specifiy:

- The condition under which points may be awarded
- How many points may be awarded

The number of points for a point-awardable condition will, upon merging,
be awarded to the initiator of a PR which fulfills the condition, if the PR reflects this awarding of points.

Players cannot obtain points using a point-awardable condition introduced in *that* PR.

Upon request of another player, the initiator of a PR must state how many points their PR adds
to their score as a result of which specific point-awardable conditions.


**353** *A Tattoo on the tongue*

The presence of at least one quote from a book, movie, TV-show, or person with a
source-annotation in an unedited comment by the initiator of a PR is a point-awardable
condition on said PR, for 0.1 points.

Players are encouraged to present a quote that matches the contents of the pull request that has not been used before in
another Pull Request.

**369** *Hash Brownie Points*

The presence of  `y` commit hashes containing an English dictionary word of at least
four consecutive letters is a point-awardable condition on a PR which contains said commit
for `y` points.

An English dictionary word is defined as a word found in the Oxford Dictionary available
[here](http://www.oxforddictionaries.com/). The default search setting of Eng (UK) is to be used as a search criterium.

If the PR is a conditional PR, the commits must not be in the parent branch for the points to be awarded.

**375** *他の言語 or diğer diller or alte limbi*

The presence of a word or sentence in either
Japanese, Turkish or Romanian and a translation in English, in an unedited comment by the initiator of a
PR is a point-awardable condition on said PR, for 0.1 points.

Uniqueness of this word or sentence is encouraged, as is correctness of the translation. 


# Point Transfers

## Mutable Rules

**341** *You scratch my back...*

Players can give points to another player through a procedure defined as a Transfer. A Transfer is defined as a
transferral of a positive number of positive points `x` from a player A (the "Sender") to a player B (the "Receiver").
In order for a Transfer to be valid, the following conditions need to be met:

- The Transfer is outlined in a Pull-Request titled: "Transfer of `x` points from A to B" where A and B are the names of
	the Sender and Recipient respectively. 
- The only change outlined in the Pull Request is a point reduction of `x` points from the Sender and a point increase
	of `x` for the Receiver.
- The Sender is the only one who can initiate the Transfer.
- The Receiver is the only one who can accept the Transfer.
- When the Transfer is initiated, the Sender has a point score of at least `x` points.
- At the time the Transfer is accepted, the Sender still has a point score of at least `x` points, so that transferring
	the `x` points will result in a point score of at least 0 for the Sender.

Pull Requests that outline a valid Transfer need not be voted on. 

Pull Requests that ouline a valid Transfer can in all other aspects be regarded as non rule-change Pull Requests.

**366** *Tit for Tat*

The Sender of a Transfer X can add extra conditions to Transfer X in addition to those outlined in the rules. If these
extra conditions contradict the conditions in the rules, the Transfer can never be valid.
The Receiver must post a comment describing the resolution of these extra conditions with validity as a result, before
he can accept the Transfer.

# Criminal Law

## Mutable Rules

**307** *Yes, I am in Fact Judging You*

If at least one player disagrees about the legality of a move or the interpretation
or application of a rule, this player may _invoke Judgement_. See below for the
definition.

When a player invokes Judgement, a Judge is selected to decide the question.
The Judge is selected from the set of players that is eligible to become
Judge.
Players are in this set when all of the following constraints are met:
 1. The player is not the most recent editor of (one of) the rule(s) that is the
 		subject of the disagreement.
 2. The player is not currently a Judge in another Judgement.

If this set contains multiple players, the player with the alphanumeric GitHub
handle previous (with wrap-around) to the player who invoked Judgement is
selected from this group.
If this set is empty, the rules above are removed one-by-one in bottom-to-top order until
the set is no longer empty.
If all these rules have been removed, a Judge is decided by majority vote.
If the majority vote does not produce a conclusive result, a Judge is selected
at random by @Jason-Statham.

_Invoking Judgement_ means a player who is currently not a Judge submits an
issue labelled "Judgement".

The Judge's Judgment may be overruled only by a unanimous vote of the other players
taken before a turn has ended after the Judge's Judgment. If a Judge's Judgment is overruled,
then the player currently the Judge is no longer a Judge and the player preceding the previous 
Judge alphanumerically becomes the new Judge for the question, and so on, except that a player
having an open issue labelled "Judgement", a team-mate of a player having an open issue 
labelled "Judgement" or a player who has been a Judge since the last time Judgement has been
completed is not to be a Judge. If this excludes all players, then a Judge is decided by 
a majority vote.

When Judgment has been invoked, a player may not begin a turn without the consent of a
majority of the other players. 

New Judges are not bound by the decisions of old Judges. New Judges may,
however, settle only those questions on which the players currently disagree. All
decisions by Judges shall be in accordance with all the rules then in effect;
but when the rules are silent, inconsistent, or unclear on the point at issue,
then the Judge shall consider game-custom and the spirit of the game before
applying other standards.

Judgement is completed when the Judge has decided all questions and is not overruled. After the
Judge's Judgement has been completed, any Judge is no longer a Judge and a player who can shall 
close all open issues labelled "Judgement" in a timely fashion. 

**354** *Punish the Guilty*

If a player (unwittingly) performs an action that directly contradicts a
rule, a procedure defined as a _Trial_ can take place. A Trial is concluded with a _Verdict_
that will be enacted by someone who has this power.

**359** *Roleplaying in Court*

A Trial features three roles:

- A defendant, the player charged with the violation.
- A prosecutor.
- A jury, comprised of at least one player.

No player can take multiple roles in a single Trial, i.e. a player can not be both prosecutor and jury.

**363** *Jury Selection*

The jury in a Trial is selected in a procedure called _Jury Selection_. Jury Selection is defined as follows.
Both prosecution and defendant must call forth at least one player for jury duty. (Note: There is no uniqueness
requirement, which means a one-manned jury is still a valid jury.)

**362** *Perfect Prosecutor*

The prosecutor of a Trial is selected as follows:

- If a player accuses another player of breaking a rule, the accuser will take the role of prosecutor in the Trial.
- Else If no other method of choosing a prosecutor in a Trial is defined, the prosecutor will be selected through the
	procedure for invoking Judgement. In this procedure the defendant will take the role of the person invoking Judgement.

**371** *Ace Attorney*

A _Defense Attorney_ is a player that can be chosen by the defendant to represent him during a Trial. The player chosen
for defense attorney has the right to refuse this role. The defense attorney can only be chosen at the start of the
Trial before the jury is selected and after the requested player has accepted the role of defense attorney, the
attorney can not be replaced by another player not yet involved in the Trial.

The defendant is allowed to overrule statements by his defense attorney if done before the jury deliberation. The
defendant may also fire his defense attorney by explicitly expressing this in a comment in the Trial. After this the
defendant is the Defense Attorney in the Trial.

If the defendant feels he has not been properly represented he should use his right to appeal for this.

If the defendant chooses not to have a defense attorney, he will take the role of defense attorney in addition to his
role as defendant. This is called _Self Representation_.

**361** *The Court Room*

A Trial shall take place in a GitHub issue with the Trial label. The Trial shall be named "The people vs #githubhandle
XX" where #githubhandle is the name of the defendant and XX is the number representing how often this player has been on
Trial.

**372** *The Trial Procedure*

A Trial procedure takes place in the following way:

1. The roles are assigned through their respective processes.
2. The prosecutor will outline the actions of the defendant that he claims are in violation of the rules and demand a
	punishment in the form of a non-negative integer point reduction of the defendants point. This reduction can be of 0
	points.
3. The defense attorney is allowed to defend the actions of the defendant and can enter a plea of either _Guilty_ or
	_Not Guilty_. If a Guilty plea is entered, he can propose an alternative punishment in the form of a non-negative
	integer point reduction no larger than that of the prosecution. If a Not Guilty plea is entered, an alternative
	punishment of a zero point reduction is assumed.
4. The prosecution and jury may ask the defendant about his actions and the defendant should either answer these
	questions to the best of his abilities, or exercise his right to remain silent. Lying during a Trial is an
	offense for which a player can be put on Trial. The defense attorney can advise the defendant on whether or not these
	questions should be answered.
5. After the jury has no more questions to ask, the prosecution and defense attorney get the opportunity to present a
	closing statement with the defendant being given the last opportunity to speak. During this closing statement and
	throughout other parts of the Trial, the defense (attorney) and prosecution are allowed to confront the jury with
	previous Verdicts handed out by them or by other juries in similar cases.
6. The jury will deliberate on their Verdict.
7. Deliberation of the Verdict will happen in public in the GitHub issue, but the other participants in the Trial are no
	longer allowed to interfere in this procedure.
8. The Jury renders their Verdict in the GitHub issue.
9. If the defendant is found Guilty, the illegal actions of the defendant will be undone by someone who has this power in
	a timely fashion.
	

**358** *Review without Passion*

The Verdict of the jury is two-fold, first the guilt of the defendant must be established, secondly the punishment.
The jury shall first decide if the defendant is _Guilty_ of the offense or _Not Guilty_. 

- If no consensus on the guilt of the defendant can be established, then a voting round will take place. Only jury
	members are allowed to vote. If the voting does not result in a simple majority, the defendant will be declared Not
	Guilty.

If the jury has found the defendant to be _Guilty_, a punishment shall be decided. This punishment may not be a larger
deduction than the prosecutor's proposal and should be a reduction of at least 0 points.

- If no concensus on the final punishment can be reached by the jury, every jury member votes for a certain positive
	point reduction. The rounded average (rounded to one decimal place) of these votes will be the final verdict of the
	jury.

**357** *The Right to Appeal*

After the Verdict has been rendered the defendant has the right to _Appeal_ if at least two players eligible for jury
duty exist that did not have a role in the Trial. The Appeal is a Trial with a new jury and (if possible) the same
prosecution. If prosecution is no longer available, the procedure of invoking Judgement will be used to select a new
prosecutor for the Appeal.


**326** *Let it Go!*

As long as an issue labelled "Trial" or "Judgement" is open, no player may start a turn, regardless of what
other rules specify. Futhermore, any rule specifying that a pull request should be merged in a timely fashion shall
be read as specifying that the pull request should be merged in a timely fashion, after all issues labelled "Trial"
or "Judgement" are closed. Any player may start a vote in a separate issue to ignore a particular issue labelled 
"Trial" or "Judgement" for purposes of this rule. 
That issue will be ignored if a simple majority votes in favour of doing so.

**338** *Statue of limitations*

No player can be put on Trial for an offense committed more than 7 days (148 hours, 0 minutes and 0 seconds) ago. Similary Trials can not be reopened for appeals more than 7 days after the Verdict has been rendered by the jury.

**344** *Oi, that's cheating!*

During a Trial and a 24 hour period after the Verdict has been given, no Transfers between a member of the jury and
another player are allowed to be initiated or completed.

**350** *Safety in opening*

If the act of opening `X` is not forbidden by any other rule, then the manner in which `X` is opened can not be
considered a violation. `X` can be either a Pull Request or Issue in this rule.

An example is that if the player forgets to label an issue properly this can not be considered a
violation so long as opening an issue is not forbidden.
