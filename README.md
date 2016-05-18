Nomic: The GitHub Edition 
=========================

Nomic is a game wherein the point is to change the rules of the game. The
[original paper](http://www.earlham.edu/~peters/writing/nomic.htm) goes to great
depths explaining just why this is a fun and worthy use of time. Everyone should
at least make a stab at reading that. This file is in 
[GitHub-flavored Markdown](http://github.github.com/github-flavored-markdown/)

Player List 
-----------
1. Pim Otte (@pimotte, 3 points)
2. Stefan Hugtenburg (@MrHug, 4 points)
3. Arthur Bik (@arthurbik, 1 point)
4. Jesse Donkervliet (@jdonkervliet, 1 point)

Immutable Rules 
---------------

**101** All players must always abide by all the rules then in effect, in the
form in which they are then in effect. The rules in the Initial Set are in
effect whenever a game begins. The Initial Set consists of Rules 101-116
(immutable) and 201-214 (mutable).

**102** Initially rules in the 100's are immutable and rules in the 200's are
mutable. Rules subsequently enacted or transmuted (that is, changed from
immutable to mutable or vice versa) may be immutable or mutable regardless of
their numbers, and rules in the Initial Set may be transmuted regardless of
their numbers.

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

**105** Every player is an eligible voter. 

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

**110** In a conflict between a mutable and an immutable rule, the immutable
rule takes precedence and the mutable rule shall be entirely void. For the
purposes of this rule a proposal to transmute an immutable rule does not
"conflict" with that immutable rule.

**111** Other players may suggest amendments or argue
against the proposal before the vote. A reasonable time must be allowed for this
debate. The proponent decides the final form in which the proposal is to be
voted on and, unless the Judge has been asked to do so, also decides the time to
end debate and vote.

**112** The state of affairs that constitutes winning may not be altered from
achieving n points to any other state of affairs. The magnitude of n and the
means of earning points may be changed, and rules that establish a winner when
play cannot continue may be enacted and (while they are mutable) be amended or
repealed.

**113** A player always has the option to forfeit the game rather than continue
to play or incur a game penalty. No penalty worse than losing, in the judgment
of the player to incur it, may be imposed.

**114** There must always be at least one mutable rule. The adoption of
rule-changes must never become completely impermissible.

**115** Rule-changes that affect rules needed to allow or apply rule-changes are
as permissible as other rule-changes. Even rule-changes that amend or repeal
their own authority are permissible. No rule-change or type of move is
impermissible solely on account of the self-reference or self-application of a
rule.

**116** Whatever is not prohibited or regulated by a rule is permitted and
unregulated, with the sole exception of changing the rules, which is permitted
only when a rule or set of rules explicitly or implicitly permits it.

Mutable Rules 
-------------

**303** A player may have an infinite number of concurrent turns.
A player may start a turn regardless of the state of their other turns.
All players begin with zero points.

**202** One turn consists of proposing one rule-change and having it voted on.

**203** A rule-change is adopted if and only if at least a simple majority
of the players votes in favour of the rule-change.

**204** An adopted rule-change takes full effect at the moment of the completion
of the vote that adopted it.

**205** When a proposed rule-change is adopted, the player who proposed it
gains 1 point.

**206** Each player always has exactly one vote.

**207** The winner is the first player to achieve 200 (positive) points.

**209** If two or more mutable rules conflict with one another, or if two or
more immutable rules conflict with one another, then the rule with the lowest
ordinal number takes precedence.

If at least one of the rules in conflict explicitly says of itself that it
defers to another rule (or type of rule) or takes precedence over another rule
(or type of rule), then such provisions shall supersede the numerical method for
determining precedence.

If two or more rules claim to take precedence over one another or to defer to
one another, then the numerical method again governs.

**305** If at least one player disagrees about the legality of a move or the interpretation
or application of a rule, a Judge is to decide the question. If no player is currently a Judge,
then the player, among the players not currently having an open issue labelled "Judgement", 
with the Github handle alphanumerically previous to the player, who started an open issue labelled 
"Judgement" first amongst all players currently having an open issue labelled "Judgement", is 
to be the Judge. If all players have an open issue labelled "Judgement", then a Judge is decided by 
a majority vote.

Disagreement for the purposes of this rule may, at any time, be created by the insistence of
any player who is not a Judge by submiting an issue labelled "Judgement". This process is 
called invoking Judgment. 

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

**211** If the rules are changed so that further play is impossible, or if the
legality of a move cannot be determined with finality, or if by the Judge's best
reasoning, not overruled, a move appears equally legal and illegal, then the
player who proposed the last adopted rule wins.

This rule takes precedence over every other rule determining the winner.

**309** A rule-change is proposed by submitting a pull request, such that
merging the pull request reflects the accurate state of the game after
adoption of the rule-change. In case the rule-change has been given a number
for reference, this number must be included in the title of the pull request.

**213** A non-player can become a player by submitting a pull request which adds
their name and Github handle to the Player List.

**306** A player can vote in favor of a rule-change by commenting on the pull request
with a comment that consists only of ":+1:". Likewise, a player can vote against
a rule-change by commenting on the pull request with a comment that consists
only of ":-1:". A commit on a pull
request dated after any votes resets those votes.

If the rule-change is adopted, a player who can shall merge the pull-request
in a timely fashion, which marks completion of the vote.

**308** If a PR that outlines a rule-change contains `y` commit hashes containing an English dictionary word of at least
four consecutive letters, the proposer will be awarded `y` additional points when the PR is merged into the master
branch of pimotte/nomic.

An English dictionary word is defined as a word found in the Oxford Dictionary available
[here](http://www.oxforddictionaries.com/). The default search setting of Eng (UK) is to be used as a search criterium.

Points are only awarded if the proposer includes the `y` points in his update of his score and mentions this explicitly
in his PR.

**311** If a player (unwittingly) performs an action that directly contradicts a
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
	punishment in the form of a point reduction of the defendants point. This reduction can be of 0 points.
- The defendant is allowed to defend his actions and propose an alternative punishment in the form of a point reduction
	no larger than that of the prosecution.
- The prosecution and jury may ask the defendant about his actions and the defendant is obliged to answer these
	questions to the best of his abilities.
- After the jury has no more questions to ask, they will deliberate on the punishment. This punishment may not be a
	larger deduction than the prosecutor's proposal, nor may it be smaller than that of the defendant.
- Deliberation of the punishment will happen in public in the GitHub issue, but the defendant and prosecutor are no
	longer allowed to interfere in this procedure.
- If no concensus on the final punishment can be reached by the jury, every jury member votes for a certain point
	reduction. The rounded average (to the nearest integer) of these votes will be the final verdict of the jury.
- Once the jury has given it's verdict, it will be enacted by someone who has this power in a timely fashion.
- If at least one point is taken from the defendant's score, the defendant is pronounced _Guilty_.
- Else if no points are taken from the defendant's score, the defendant is pronounced _Not Guilty_.
- If the defendant is found Guilty, the illegal actions of the defendant will be undone by someone who has this power in
	a timely fashion.
- If at least two eligible voters exist that were not part of the Trial (i.e. no part of the jury, defense or
	prosecution), the defendant has the right to appeal the verdict in a new trial with a new jury and (if possible) the
	same prosecution. If prosecution is no longer available, the procedure of invoking Judgement will be used to select a
	prosecutor.
- During a Trial session, both prosecution and defense are allowed to refer to old Trials in their pleas for a certain
	punishment.
