import enum


class NotificationType(str, enum.Enum):
    DISABLED = "disabled"
    ME = "me"
    AGENT = "agent"
    ME_AND_AGENT = "me_and_agent"


class Technology(str, enum.Enum):
    BRICK = "brick"
    PANEL = "panel"
    AERATED_CONCRETE = "aerated_concrete"
    FRAME = "frame"


class PropertyType(str, enum.Enum):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"
    LAND = "land"


class OwnershipType(str, enum.Enum):
    PRIVATE = "private_ownership"
    STATE = "state_ownership"
    MUNICIPAL = "municipal_ownership"
    LEASEHOLD = "leasehold"
    LONG_TERM_LEASE = "long_term_lease"
    UNDER_CONSTRUCTION_SALE = "under_construction_sale"
    NEW_BUILDING_COMMISSIONED = "new_building_commissioned"
    SECONDARY_MARKET = "secondary_market"
    COOPERATIVE = "cooperative_ownership"
    INHERITANCE = "inheritance"


class Bedrooms(str, enum.Enum):
    STUDIO = "studio"
    ONE = "one_bedroom"
    TWO = "two_bedrooms"
    THREE_OR_MORE = "three_or_more_bedrooms"
    DUPLEX = "duplex"


class Bathrooms(str, enum.Enum):
    SEPARATE = "separate_bathrooms"
    COMBINED = "combined_bathroom"


class Heating(str, enum.Enum):
    CENTRAL = "central"
    INDIVIDUAL_GAS = "individual_gas"
    INDIVIDUAL_ELECTRIC = "individual_electric"
    AUTONOMOUS = "autonomous"


class Commission(int, enum.Enum):
    LOW = 30000
    MEDIUM = 60000
    HIGH = 120000


class ApartmentCondition(str, enum.Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    SATISFACTORY = "satisfactory"
    NEEDS_RENOVATION = "needs_renovation"
    BAD = "bad"


class Finishing(str, enum.Enum):
    NO_FINISHING = "no_finishing"
    ROUGH = "rough_finishing"
    PARTIALLY = "partially_finished"
    PRE = "pre_finished"
    FULLY = "fully_finished"


class Rooms(int, enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10


class CallMethod(str, enum.Enum):
    SMS = "sms"
    PHONE = "phone"
    PHONE_AND_SMS = "phone_and_sms"


class Action(str, enum.Enum):
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"
