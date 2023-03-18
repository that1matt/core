"""Constants for the Generac PWRView integration."""
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import Platform, UnitOfEnergy, UnitOfPower

DOMAIN = "generac_pwrview"
DEFAULT_NAME = "Generac PWRView"

PLATFORMS: list[Platform] = [Platform.SENSOR]

# For “cts (An array of 4 CTs.)” the following applies:
# ct: CT enumeration
# p_W: Real power in watts
# q_Var: Reactive power in volt-amps reactive
# v_V: Voltage in volts

CT_SENSORS = (
    SensorEntityDescription(
        key="CT1",
        name="CT 1",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
    SensorEntityDescription(
        key="CT2",
        name="CT 2",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
    SensorEntityDescription(
        key="CT3",
        name="CT 3",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
    SensorEntityDescription(
        key="CT4",
        name="CT 4",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
)

# For “channels (Array containing information for [up to] the six logical channels.)” the following applies:
# type: Channel type in string format. Possible values are: PHASE_A_CONSUMPTION, PHASE_B_CONSUMPTION, PHASE_C_CONSUMPTION, NET, GENERATION, CONSUMPTION, SUBMETER.
# ch: Channel number
# eImp_Ws: Imported energy in watt-seconds
# eExp_Ws: Exported energy in watt-seconds
# p_W: Real power in watts
# q_VAR: Reactive power in volt-amps reactive
# v_V: Voltage in volts
# label: User defined channel label. Only returned for SUBMETER type channels.
CHANNEL_SENSORS = (
    SensorEntityDescription(
        key="phase_a_consumption",
        name="Phase A Consumption",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
    SensorEntityDescription(
        key="phase_b_consumption",
        name="Phase B Consumption",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
    SensorEntityDescription(
        key="net",
        name="Net",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
    SensorEntityDescription(
        key="generation",
        name="Generation",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
    SensorEntityDescription(
        key="consumption",
        name="Consumption",
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.POWER,
    ),
)