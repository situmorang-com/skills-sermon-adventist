# Wire the profile through generation so it cannot be ignored

Type: task
Status: resolved
Blocked by: 03

## Question

The core defect: class profile is collected at Step 1, printed in the header, and **never used**
— three mentions in 635 lines, zero downstream branching. Q6 chose a per-profile section in the
guide, which risks repeating exactly that failure unless generation is forced to apply it.

Apply:

- Step 1's profile list becomes the six from Q10: deaf, young adults, adults, seeker,
  baptismal, mixed. Today it offers adults / young adults / youth / seekers / mixed — no deaf
  option at all, and youth is now absorbed.
- The matching profile subsection is **emitted into Section 3**, immediately before the timed
  table (Q13), because a ninth section is forbidden by the eight-step colour ramp.
- A Final Pass item asserting the emitted section matches the stated profile — the mitigation
  promised when Q6(a) was chosen over generator-wide branching.
- HTML markup contract entry for the emitted block, in both languages.
- Anti-pattern: never collect an input the output ignores.

## Answer

The collect-and-discard defect is closed. Class profile now changes the guide in five places
instead of none.

**Applied:**

- **Step 1's enum is the six** (Q10), with `deaf, signed` added and `youth` absorbed into young
  adults. The field's note now says it drives Section 3's profile block, "so it is never a
  decorative answer".
- **The profile block is emitted first in Section 3**, before the hook and the plan table.
  Slightly earlier than Q13's "immediately before the timed table": the hook is itself
  profile-dependent — consent-based reading turns for young adults, gaze for a deaf class — so
  the teacher has to know the room before reading the hook, not after.
- **Template gains `.profile`**, modelled on `.tonight`'s geometry but in **techelet**: gold is
  reserved for Spirit of Prophecy and scarlet for cautions, and the profile is structural
  information about the room rather than part of the lesson's argument. Chip defaults to "Class
  profile" in English, overridden by `data-label="Profil kelas"`. No hex outside the theme
  blocks, so the mono toggle stays clean.
- **Markup contract row** added, stating the block carries only what *changes* for this class.
- **Final Pass item 12** asserts the block is present, is first in Section 3, and matches the
  profile actually given, and explicitly fails a guide whose profile block restates the general
  advice. For a deaf class it also requires read-slots separated from sign-slots, which is the
  hook into ticket 11.
- **Anti-pattern:** "Never collect an input the output ignores. Class profile was asked for at
  Step 1, printed in the header, and used nowhere else for the life of this skill. If an input
  does not change the guide, either wire it through or stop asking for it."

**One defect caught in verification:** the enum said "seeker/visitor present" while the
subsection heading reads "Seeker or visitor present". Final Pass 12 requires matching the
profile by name, so a near-miss would have made the check unrunnable. Aligned.

Also renumbered the Final Pass tail: inserting item 12 had left two items numbered 13.

**Not done:** no guide has been regenerated against this yet. The first real test is next week's
lesson, where the profile actually has to produce a different Section 3.
