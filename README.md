Nomic: The GitHub Edition 
=========================

Nomic is a game wherein the point is to change the rules of the game. The
[original paper](http://www.earlham.edu/~peters/writing/nomic.htm) goes to great
depths explaining just why this is a fun and worthy use of time. Everyone should
at least make a stab at reading that. This file is in 
[GitHub-flavored Markdown](http://github.github.com/github-flavored-markdown/)

Player List 
-----------
1. Pim Otte (@pimotte, 8 points)
2. Stefan Hugtenburg (@MrHug, 10 points)
3. Arthur Bik (@arthurbik, 2 point)
4. Jesse Donkervliet (@jdonkervliet, 1 point)

# Rules

## Immutable Rules 

**101** All players must always abide by all the rules then in effect, in the
form in which they are then in effect. The rules in the Initial Set are in
effect whenever a game begins. The Initial Set consists of Rules 101-116
(immutable) and 201-214 (mutable).

**102** Initially rules in the 100's are immutable and rules in the 200's are
mutable. Rules subsequently enacted or transmuted (that is, changed from
immutable to mutable or vice versa) may be immutable or mutable regardless of
their numbers, and rules in the Initial Set may be transmuted regardless of
their numbers.

**110** In a conflict between a mutable and an immutable rule, the immutable
rule takes precedence and the mutable rule shall be entirely void. For the
purposes of this rule a proposal to transmute an immutable rule does not
"conflict" with that immutable rule.

**116** Whatever is not prohibited or regulated by a rule is permitted and
unregulated, with the sole exception of changing the rules, which is permitted
only when a rule or set of rules explicitly or implicitly permits it.

## Mutable Rules

**209** If two or more mutable rules conflict with one another, or if two or
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

**103** A rule-change is any of the following: (1) the enactment, repeal, or
amendment of a mutable rule; (2) the enactment, repeal, or amendment of an
amendment of a mutable rule; or (3) the transmutation of an immutable rule into
a mutable rule or vice versa.

(Note: This definition implies that, at least initially, all new rules are
mutable; immutable rules, as long as they are immutable, may not be amended or
repealed; mutable rules, as long as they are mutable, may be amended or
repealed; any rule of any status may be transmuted; no rule is absolutely immune
to change.)

**104** All rule-changes proposed in the proper way shall be voted on. They will
be adopted if and only if they receive the required number of votes.

**106** All proposed rule-changes shall be written down before they are voted
on. If they are adopted, they shall guide play in the form in which they were
voted on.

**107** No rule-change may take effect earlier than the moment of the completion
of the vote that adopted it, even if its wording explicitly states otherwise. No
rule-change may have retroactive application.

**108** Each proposed rule-change shall be given a number for reference. The
numbers shall begin with 301, and each rule-change proposed in the proper way
shall receive the next successive integer, whether or not the proposal is
adopted.

If a rule is repealed and reenacted, it receives the number of the proposal to
reenact it. If a rule is amended or transmuted, it receives the number of the
proposal to amend or transmute it. If an amendment is amended or repealed, the
entire rule of which it is a part receives the number of the proposal to amend
or repeal the amendment.

**109** Rule-changes that transmute immutable rules into mutable rules may be
adopted if and only if the vote is unanimous among the eligible voters.
Transmutation shall not be implied, but must be stated explicitly in a proposal
to take effect.

**114** There must always be at least one mutable rule. The adoption of
rule-changes must never become completely impermissible.

**115** Rule-changes that affect rules needed to allow or apply rule-changes are
as permissible as other rule-changes. Even rule-changes that amend or repeal
their own authority are permissible. No rule-change or type of move is
impermissible solely on account of the self-reference or self-application of a
rule.

**203** A rule-change is adopted if and only if at least a simple majority
of the players votes in favour of the rule-change.

**204** An adopted rule-change takes full effect at the moment of the completion
of the vote that adopted it.

## Mutable Rules

**309** A rule-change is proposed by submitting a pull request, such that
merging the pull request reflects the accurate state of the game after
adoption of the rule-change. In case the rule-change has been given a number
for reference, this number must be included in the title of the pull request.

**312** In addition to other types of valid rule-changes outlined in the rules, a rule-change may also consist of moving
a part of an existing mutable rule into a new mutable rule. In order for this rule-change to be valid, the phrasing of
the new rule must be identical to the phrasing of the clause or sentence in the old rule and the new rule must be
self-contained, meaning it does not require a reference to the old rule to be understood. Similarly the old rule must
still be self-contained and sensible with part of it removed.

# Non-Changes

## Mutable Rules

**319** Both players and non-players are allowed to submit a pull request to master on pimotte/nomic, 
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

**105** Every player is an eligible voter. 

**111** Other players may suggest amendments or argue
against the proposal before the vote. A reasonable time must be allowed for this
debate. The proponent decides the final form in which the proposal is to be
voted on and, unless the Judge has been asked to do so, also decides the time to
end debate and vote.

**205** When a proposed rule-change is adopted, the player who proposed it
gains 1 point.

**315** Each eligible voter always has exactly one vote.

# Mutable Rules

**318** A player can vote in favor of a rule-change by commenting on the pull request
with a comment that consists only of ":+1:". Likewise, a player can vote against
a rule-change by commenting on the pull request with a comment that consists
only of ":-1:". 

A commit on a pull request dated after any votes resets those votes, 
unless this commit is a merge commit resulting from a merge from master on pimotte/nomic to 
the source branch of the pull request and does not alter the proposed rule-change.

During a simple majority vote, a player may warn the other players that the vote is going to end.
If this warning raises no objections and a reasonable time has passed, the vote ends and the rule
is adopted when a majority of the votes that are cast are in favor of the rule-change. 
A reasonable time in this context is at least 72 hours and is at least enough time for the warning
to reach all other players and for all other players to react to the warning. 
An objection can be raised by any player at any time, this includes the option to raise objections
to future warnings.

If the rule-change is adopted, a player who can shall merge the pull request
in a timely fashion, which marks completion of the vote.

**321** A vote can be retracted by commenting on the pull request with a comment that 
consists only of ":wave:". This will retract any votes made by the player that were made before
this comment. A vote can only be retracted as long as it is valid and the rule-change is not
yet adopted or rejected.

**313** Any vote through a comment on a pull request is invalid, unless one of the
comments above the vote contains a word or sentence in either Japanese or Turkish 
and a translation in English. Uniqueness of this word or sentence is encouraged,
as is correctness of the translation. There are no sanctions for voting
when this rule disallows it, regardless of what other rules specify, 
if and only if voting in this way only violates this rule.

**323** It may be assumed that the proposer of a rule-change is always in favour of this rule-change and thus has
cast an implicit vote in favour of the rule-change. 
An explicit vote through the procedures outlined in the rules replaces this implicit vote in favour.
If the implicit vote is not overwritten with an explicit vote, the validity of the implicit vote is held to the same
requirements as any other vote. For the purpose of validity checking, it can be considered an unwritten comment placed
after all comments on the PR before the merging comment of the PR.

# Win Condition & Participation

## Immutable Rules

**112** The state of affairs that constitutes winning may not be altered from
achieving n points to any other state of affairs. The magnitude of n and the
means of earning points may be changed, and rules that establish a winner when
play cannot continue may be enacted and (while they are mutable) be amended or
repealed.

**113** A player always has the option to forfeit the game rather than continue
to play or incur a game penalty. No penalty worse than losing, in the judgment
of the player to incur it, may be imposed.

## Mutable Rules

**207** The winner is the first player to achieve 200 (positive) points.

**211** If the rules are changed so that further play is impossible, or if the
legality of a move cannot be determined with finality, or if by the Judge's best
reasoning, not overruled, a move appears equally legal and illegal, then the
player who proposed the last adopted rule wins.

This rule takes precedence over every other rule determining the winner.

**213** A non-player can become a player by submitting a pull request which adds
their name and Github handle to the Player List.

# Turns

## Mutable Rules 

**303** A player may have an infinite number of concurrent turns.
A player may start a turn regardless of the state of their other turns.

**320** All players begin with zero points.

**202** One turn consists of proposing one rule-change and having it voted on.

# Points

## Mutable Rules

**308** If a PR that outlines a rule-change contains `y` commit hashes containing an English dictionary word of at least
four consecutive letters, the proposer will be awarded `y` additional points when the PR is merged into the master
branch of pimotte/nomic.

An English dictionary word is defined as a word found in the Oxford Dictionary available
[here](http://www.oxforddictionaries.com/). The default search setting of Eng (UK) is to be used as a search criterium.

Points are only awarded if the proposer includes the `y` points in his update of his score and mentions this explicitly
in his PR.

# Criminal Law

## Mutable Rules

**307** If at least one player disagrees about the legality of a move or the interpretation
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

**324** If a player (unwittingly) performs an action that directly contradicts a
rule, a procedure defined as a _Trial_, with the rule-breaking player as the defendant, will take place. A Trial is
defined as follows.

- Every Trial takes places on GitHub in a new issue with the "Trial" label.
- Every Trial features a defendant.
- Every Trial features a prosecutor.
- Every Trial features a jury, comprised of at least one player.
- No player can take multiple roles in a single trial, i.e. a player can not be both prosecutor and jury.
- Both prosecution and defendant must call forth at least one player for jury duty. (Note: There is no uniqueness
	requirement, which means a one-manned jury is still a valid jury.)
- Every Trial shall have the name "The people vs #githubhandle XX" where #githubhandle is the name of the defendant and
	XX is the number representing how often this player has been on Trial.
- If a player accuses another player of breaking a rule, the accuser will take the role of prosecutor in the Trial.
- Else If no other method of choosing a prosecutor in a Trial is defined, the prosecutor will be selected through the
	procedure for invoking Judgement. In this procedure the defendant will take the role of the person invoking Judgement.
- The prosecutor will outline the actions of the defendant that he claims are in violation of the rules and demand a
	punishment in the form of a non-negative integer point reduction of the defendants point. This reduction can be of 0
	points.
- The defendant is allowed to defend his actions and can plead either _Guilty_ or _Not Guilty_. If he pleads Guilty, he
	can propose an alternative punishment in the form of a non-negative integer point reduction no larger than that of the
	prosecution. If he pleads Not Guilty, an alternative punishment of a zero point reduction is assumed.
- The prosecution and jury may ask the defendant about his actions and the defendant should either answer these
	questions to the best of his abilities, or exercise his right to remain silent. Lying during a Trial is an
	offense for which a player can be put on Trial.
- After the jury has no more questions to ask, they will deliberate on their _Verdict_.
- Deliberation of the Verdict will happen in public in the GitHub issue, but the defendant and prosecutor are no
	longer allowed to interfere in this procedure.
- The Verdict of the jury is two-fold, first the guilt of the defendant must be established, secondly the punishment.
	- The jury shall first decide if the defendant is _Guilty_ of the offense or _Not Guilty_. 
	- If no consensus on the guilt of the defendant can be established, then a voting round will take place. Only jury
		members are allowed to vote. If the voting does not result in a simple majority, the defendant will be declared Not
		Guilty.
	- If the jury has found the defendant to be _Guilty_, a punishment shall be decided. This punishment may not be a
		larger deduction than the prosecutor's proposal, nor may it be smaller than that of the defendant.
	- If no concensus on the final punishment can be reached by the jury, every jury member votes for a certain point
		reduction. The rounded average (to the nearest integer) of these votes will be the final verdict of the jury.
- If the defendant is found Guilty, the illegal actions of the defendant will be undone by someone who has this power in
	a timely fashion.
- Once the jury has given it's Verdict, it will be enacted by someone who has this power in a timely fashion.
- If at least two eligible voters exist that were not part of the Trial (i.e. no part of the jury, defense or
	prosecution), the defendant has the right to appeal the verdict in a new trial with a new jury and (if possible) the
	same prosecution. If prosecution is no longer available, the procedure of invoking Judgement will be used to select a
	new prosecutor.
- During a Trial session, both prosecution and defense are allowed to refer to old Trials in their pleas for a certain
	punishment.

