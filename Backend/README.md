# Sibling Rivalry

REWARD CALCULATOR (should be between -1 to 1)

- Reward function = 0.8 * score + 0.1 * damage + 0.1 * health produced
- score = multiplier * (passively + actively) / (2 * bm_health)
- damage = multiplier * (passively + actively) / (2 * bm_health)
- health produced = (passively + actively) / (2 * bm_health)


- Value of Steel
  - Standard: cost of battle mage; adds to health production

- Value of Gunpowder
  - Standard: damage left for cannon/damage of bomb; adds to damage production

- Ore
  - Also translated to health or damage production defined by anvils.

- Active actions:
  - Killing invader
  - Collecting resource
  - Purchasing upgrade / trade / cannon / anvil / furance / battlemage / alchemy table
- Passive actions:
  - Killing invader
  - Producing Ore


TECHNICAL DEBT

- Refractor/extract all reward functions
- Replace attribute sorting in addToInventory
  - solution1: 2-sum + find min?
  - solution2: use heap
- Create mergable interface for typing
  - Anvil, Cannon, Furance, InvaderPart, Resource, Weapon
- Create damage interface for typing
- Extract action functions
  - solution1: strategy pattern
