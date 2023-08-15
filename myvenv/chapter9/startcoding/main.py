# 1. import package.module
import unit.character
unit.character.test()

# 2. from package import module
from unit import item
item.test()

# 3. from package import *
from unit import *
character.test()
item.test()
monster.test()

# 4. import package
import unit
unit.character.test()
unit.item.test()
unit.monster.test()