# Facilitating discussion in a deaf, signed Sabbath School class

Type: research
Status: resolved

## Question

`teaching-methods.md` runs 185 lines on facilitation and contains nothing on a deaf or signed
class, yet it is one of six profiles the teacher rotates through. What is actually known about
running a *discussion* — not a lecture — in a signed congregation?

Specifically:

- Turn-taking. How is the floor handed between members when the channel is visual and everyone
  must be able to see the speaker? What replaces "go around the circle"?
- Silence. The guide currently prescribes four to six seconds of silence after a real question.
  Does that read the same way in a signed room, or does visible stillness mean something else?
- Attention. Established in charting (Q11) that the class reads Scripture **together off a
  screen**, so text and signing are sequential, not simultaneous. What else is single-channel?
- Small groups of three, which the guide uses to solve both the dominant talker and the silent
  class. Does that work in a signed room, or does it fragment sightlines?
- Simplified Indonesian. What does register control actually mean for a deaf Indonesian
  congregation — reading level, sentence length, avoidance of idiom?

Adventist deaf-ministry sources are preferred where they exist. General deaf-education
literature on classroom discussion is acceptable and should be labelled as such. Distinguish
findings that are evidenced from findings that are one practitioner's practice.

Do not invent practice. Where the answer is not known, say so — the charting session already
guessed wrong once here (assumed interpreter lag; the class in fact reads together off a
screen).

## Output

Write findings to `.scratch/listener-methodology/research/deaf-class-facilitation.md`.

## Answer

Findings: [`research/deaf-class-facilitation.md`](../research/deaf-class-facilitation.md).

**No Adventist material on facilitating a deaf class exists.** ADM/3ADM/*Ministry*/NAD publish
on befriending deaf members, interpreting, and simplified print. On turn-taking, questioning,
wait time or group work in a deaf Sabbath School: nothing. So the subsection will be ours,
built on general deaf-education research, and must say so.

**Turn-taking is the best-answered question and gives us a better dominant-talker move than we
have.** Mather's classroom gaze taxonomy (via Singleton & Crume 2022) treats teacher gaze as the
turn-allocation system: arc sweep = question is for everyone, fixed midpoint = same, gaze at one
person = tells everyone else it is not their turn. The teacher's eyes are the microphone.
Members bid by waving or table-thumping, and a teacher **refuses a bid by withholding eye
contact** — quieter and more documented than the small-groups-of-three the guide currently
prescribes for that problem.

**Silence survives, but our number is borrowed.** de Vos, Torreira & Levinson (2015) measured
NGT turn gaps at median 269 ms, inside the spoken range, so a signed pause is as marked as a
spoken one. But no signed-classroom wait-time research exists; our 4–6 seconds comes from
Rowe's hearing classrooms and must be labelled as borrowed. The real difference: a signing
teacher has **no neutral place to put her eyes** during the pause, because looking away ends the
question.

**Attention is strictly sequential, and this changes the timed plan.** Marschark et al. (2006)
eye-tracking found deaf students showed no successful divided attention, only switching. The
screen finding generalises: handouts, note-taking, another member's turn and the teacher's gaze
are one channel. **Read-slots and sign-slots must be separate blocks**, never concurrent.

**Register: the denomination has done checkable work, in English only.** An Easy Reading edition
is fetchable from the API the skill already uses — verified `en/quarterlies/2026-03-er`, and its
Lesson 9 Sunday opens "What is Paul thankful for in these verses?" against the standard
edition's "What is the reason for Paul's attitude of thanksgiving here?" Eight concrete
transformations were extracted by diffing the two. **No Indonesian Easy Reading exists** — I
doubted this and re-checked; the agent was right, see the API note below. Carried to a new
ticket.

**Rejected, and the rejection should stick:** a 2001 *Ministry* article says deaf people "may
find it challenging to think in the abstract." The same denomination contradicts it in 2016.
Register control is **language access, not cognitive capacity**. The guide carries the
simplification and drops that rationale; a future session should not reintroduce it.

**Limits to state in the subsection:** every finding is ASL/NGT/BSL/Libras. **Nothing on
Bisindo.** Nothing on Efata Tuli or any Indonesian Adventist deaf congregation. No evidence at
all on small groups in a signed class.

**Retry candidates, both publisher-blocked:** a Cogent Education 2023 study on deaf teaching
strategies in Jakarta special schools (most locally relevant paper found), and the figure that
Indonesian deaf 17–18-year-olds write at a hearing 9–10-year-old level — held at second hand and
flagged unverified.
