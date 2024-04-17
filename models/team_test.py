from Team import Team
from Team import Base

team1 = Team("townies", "turnt")

print(team1.__repr__())
print(Base.metadata)
print(team1.metadata)
