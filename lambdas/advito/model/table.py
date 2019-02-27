# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, JSON, Numeric, String, Table, Text, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AdvitoApplication(Base):
    __tablename__ = 'advito_application'

    id = Column(BigInteger, primary_key=True)
    application_name = Column(String(32), nullable=False)
    application_full = Column(String(64), nullable=False)
    application_tag = Column(String(8), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


class AdvitoGroup(Base):
    __tablename__ = 'advito_group'

    id = Column(BigInteger, primary_key=True)
    group_name = Column(String(64), nullable=False)
    group_tag = Column(String(8))
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)
    is_assignable = Column(Boolean, nullable=False, server_default=text("true"))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


class Alert(Base):
    __tablename__ = 'alert'

    id = Column(BigInteger, primary_key=True)
    application_id = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger)
    role_id = Column(BigInteger)
    client_id = Column(BigInteger)
    alert_status = Column(String(32), nullable=False, server_default=text("'Active'::character varying"))
    alert_type = Column(String(32), nullable=False)
    alert_timestamp = Column(DateTime, nullable=False)
    alert_expiration_timestamp = Column(DateTime)
    is_deleted = Column(Boolean, nullable=False, server_default=text("false"))
    alert_text = Column(String(256), nullable=False)
    alert_detail = Column(String(256))
    alert_note = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


class Client(Base):
    __tablename__ = 'client'

    id = Column(BigInteger, primary_key=True)
    client_name = Column(String(32), nullable=False)
    client_name_full = Column(String(64), nullable=False)
    client_tag = Column(String(8), nullable=False)
    client_code = Column(String(32))
    lanyon_client_code = Column(String(16))
    gcn = Column(String(16))
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    logo_path = Column(String(128))
    description = Column(Text)
    industry = Column(String(64))
    default_currency_code = Column(String(8))
    default_distance_units = Column(String(32))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


class GeoContinent(Base):
    __tablename__ = 'geo_continent'

    id = Column(BigInteger, primary_key=True)
    continent_name = Column(String(32), nullable=False, unique=True)
    continent_tag = Column(String(8), nullable=False)
    continent_code = Column(String(4), nullable=False, unique=True)
    note = Column(Text)
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


class GeoRegionGroup(Base):
    __tablename__ = 'geo_region_group'

    id = Column(BigInteger, primary_key=True)
    region_group_name = Column(String(32), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    note = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


class ReasonCodeGlobal(Base):
    __tablename__ = 'reason_code_global'
    __table_args__ = (
        UniqueConstraint('code_type', 'reason_code_global'),
    )

    id = Column(BigInteger, primary_key=True)
    code_type = Column(String(16), nullable=False)
    reason_code_global = Column(String(8), nullable=False)
    code_description = Column(String(64), nullable=False)
    note = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


t_temp_import_agency = Table(
    'temp_import_agency', metadata,
    Column('product_type', String(255)),
    Column('client_name', String(255)),
    Column('record_key', String(255)),
    Column('global_customer_number', String(255)),
    Column('client_code', String(255)),
    Column('locator', String(255)),
    Column('traveler', String(255)),
    Column('invoice_date', String(255)),
    Column('invoice_number', String(255)),
    Column('agency', String(255)),
    Column('agency_number', String(255)),
    Column('booking_source', String(255)),
    Column('booking_agent_id', String(255)),
    Column('local_reason_code', String(255)),
    Column('local_reason_code_description', String(255)),
    Column('global_reason_code', String(255)),
    Column('global_reason_code_description', String(255)),
    Column('ratetype_code', String(255)),
    Column('rate_type_description', String(255)),
    Column('refund_indicator', String(255)),
    Column('exchange_indicator', String(255)),
    Column('credit_card_number', String(255)),
    Column('credit_card_type', String(255)),
    Column('credit_card_expiration', String(255)),
    Column('traveler_country', String(255)),
    Column('ticketing_country', String(255)),
    Column('int_dom', String(255)),
    Column('travel_sector', String(255)),
    Column('regional_indicator', String(255)),
    Column('round_trip_indicator', String(255)),
    Column('shortlong_haul_indicator', String(255)),
    Column('mileage', String(255)),
    Column('original_document_number', String(255)),
    Column('ticket_confirmation_number', String(255)),
    Column('net_count', String(255)),
    Column('travel_start_date', String(255)),
    Column('trip_length', String(255)),
    Column('days_advance_purchase', String(255)),
    Column('days_advance_purchase_group', String(255)),
    Column('origin_city', String(255)),
    Column('destination_city', String(255)),
    Column('vendor', String(255)),
    Column('service_description', String(255)),
    Column('service_category', String(255)),
    Column('daily_rate_minus_tax_usd', String(255)),
    Column('tax_amount_usd', String(255)),
    Column('total_invoice_amount_usd', String(255)),
    Column('low_fare_usd', String(255)),
    Column('full_fare_usd', String(255)),
    Column('fare_before_discount_usd', String(255)),
    Column('amount_lost_usd', String(255)),
    Column('full_fare_savings_usd', String(255)),
    Column('contract_savings_usd', String(255)),
    Column('cost_center', String(255)),
    Column('department', String(255)),
    Column('employee_id', String(255)),
    Column('employee_level', String(255)),
    Column('line_of_business', String(255)),
    Column('subline_of_business', String(255))
)


class TempImportAirport(Base):
    __tablename__ = 'temp_import_airport'

    airport_code = Column(String(255))
    airport_name = Column(String(255))
    airport_address = Column(String(255))
    latitude = Column(String(255))
    longitude = Column(String(255))
    airport_name2 = Column(String(255))
    airport_type = Column(String(255))
    city_code = Column(String(255))
    city_name = Column(String(255))
    state_code = Column(String(255))
    state_name = Column(String(255))
    country_code = Column(String(255))
    country_name = Column(String(255))
    subregion_code = Column(String(255))
    subregion_name = Column(String(255))
    subregion_name_short = Column(String(255))
    region_code = Column(String(255))
    region_name = Column(String(255))
    id = Column(String(255), primary_key=True)


t_temp_import_reason_codes = Table(
    'temp_import_reason_codes', metadata,
    Column('agency', String(255)),
    Column('agency_number', String(255)),
    Column('booking_source', String(255)),
    Column('booking_agent_id', String(255)),
    Column('local_reason_code', String(255)),
    Column('local_reason_code_desc', String(255)),
    Column('global_reason_code', String(255)),
    Column('global_reason_code_desc', String(255))
)


class TempStoryAir01Barchart(Base):
    __tablename__ = 'temp_story_air01_barchart'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)


t_temp_story_air01_barchart_data = Table(
    'temp_story_air01_barchart_data', metadata,
    Column('barchartid', BigInteger),
    Column('category', String(255)),
    Column('value', Integer),
    Column('change', String(255))
)


class TempStoryAir01Kpi(Base):
    __tablename__ = 'temp_story_air01_kpi'

    title = Column(String(255), primary_key=True)
    kpi_value = Column(Integer)
    delta = Column(Float)
    change = Column(String(255))
    kpi_type = Column(String(255))
    icon = Column(String(255))
    percent = Column(Float)


class TempStoryAir01Location(Base):
    __tablename__ = 'temp_story_air01_location'

    id = Column(BigInteger, primary_key=True)
    thickness = Column(Integer)
    height = Column(Float)
    opacity = Column(Float)
    _from = Column('from', String(255))
    to = Column(String(255))


class TempStoryAir01LocationCoord(Base):
    __tablename__ = 'temp_story_air01_location_coord'

    id = Column(BigInteger, primary_key=True)
    locationid = Column(BigInteger, nullable=False)
    latitude = Column(Numeric(10, 7), nullable=False)
    longitude = Column(Numeric(10, 7), nullable=False)


class TempStoryAir02Bar(Base):
    __tablename__ = 'temp_story_air02_bar'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255))
    type = Column(String(255))


class TempStoryAir02BarDatum(Base):
    __tablename__ = 'temp_story_air02_bar_data'

    id = Column(BigInteger, primary_key=True)
    barid = Column(BigInteger)
    category = Column(String(255))
    value = Column(Integer)
    change = Column(String(255))


class TempStoryAir02Kpi(Base):
    __tablename__ = 'temp_story_air02_kpi'

    title = Column(String(255), primary_key=True)
    value = Column(Integer)
    delta = Column(Integer)
    change = Column(String(255))
    type = Column(String(255))
    icon = Column(String(255))
    percent = Column(Float)


class TempStoryAir02Location(Base):
    __tablename__ = 'temp_story_air02_location'

    id = Column(BigInteger, primary_key=True)
    thickness = Column(Integer)
    height = Column(Float)
    opacity = Column(Float)
    _from = Column('from', String(255))
    to = Column(String(255))


class TempStoryAir02LocationCoord(Base):
    __tablename__ = 'temp_story_air02_location_coord'

    id = Column(BigInteger, primary_key=True)
    locationid = Column(BigInteger, nullable=False)
    latitude = Column(Numeric(10, 7), nullable=False)
    longitude = Column(Numeric(10, 7), nullable=False)


class TempStoryAir03Category(Base):
    __tablename__ = 'temp_story_air03_category'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255))
    icon = Column(String(255))
    total = Column(Integer)


class TempStoryAir03Subcategory(Base):
    __tablename__ = 'temp_story_air03_subcategory'

    id = Column(BigInteger, primary_key=True)
    categoryid = Column(BigInteger)
    name = Column(String(255))
    value = Column(String(255))
    delta = Column(String(255))
    color = Column(String(255))
    percent = Column(Float)


class TempStoryAir04Bar(Base):
    __tablename__ = 'temp_story_air04_bar'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255))
    type = Column(String(255))


class TempStoryAir04BarDatum(Base):
    __tablename__ = 'temp_story_air04_bar_data'

    id = Column(BigInteger, primary_key=True)
    barid = Column(BigInteger)
    category = Column(String(255))
    change = Column(String(255))
    value = Column(Integer)


class TempStoryAir04Category(Base):
    __tablename__ = 'temp_story_air04_category'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255))
    icon = Column(String(255))
    total = Column(Integer)


class TempStoryAir04Subcategory(Base):
    __tablename__ = 'temp_story_air04_subcategory'

    id = Column(BigInteger, primary_key=True)
    categoryid = Column(BigInteger)
    name = Column(String(255))
    value = Column(Integer)
    delta = Column(String(255))
    color = Column(String(255))
    percent = Column(Float)


t_temp_story_air05_airport = Table(
    'temp_story_air05_airport', metadata,
    Column('category', String(255)),
    Column('value', Integer),
    Column('prop', String(255))
)


class TempStoryAir05Color(Base):
    __tablename__ = 'temp_story_air05_colors'

    id = Column(BigInteger, primary_key=True)
    section = Column(String(255), nullable=False)
    color_order = Column(Integer)
    color = Column(String(16))


t_temp_story_air05_country = Table(
    'temp_story_air05_country', metadata,
    Column('category', String(255)),
    Column('value', Integer),
    Column('prop', String(255)),
    Column('nextProp', String(255))
)


class TempStoryAir05Datum(Base):
    __tablename__ = 'temp_story_air05_data'

    id = Column(BigInteger, primary_key=True)
    category = Column(String(255))
    value = Column(Integer)
    prop = Column(String(255))
    nextProp = Column(String(255))


class TempStoryAir05Static(Base):
    __tablename__ = 'temp_story_air05_static'

    id = Column(BigInteger, primary_key=True)
    section_label = Column(String(64), nullable=False)
    section_json = Column(JSON, nullable=False)


class TempStoryHotel01Bar(Base):
    __tablename__ = 'temp_story_hotel01_bar'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255))
    type = Column(String(255))


class TempStoryHotel01BarDatum(Base):
    __tablename__ = 'temp_story_hotel01_bar_data'

    id = Column(BigInteger, primary_key=True)
    barid = Column(BigInteger)
    category = Column(String(255))
    value = Column(Integer)
    delta = Column(Integer)
    change = Column(String(255))
    percent = Column(Float)


class TempStoryHotel01Kpi(Base):
    __tablename__ = 'temp_story_hotel01_kpi'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255))
    value = Column(Integer)
    delta = Column(Integer)
    change = Column(String(255))
    type = Column(String(255))
    icon = Column(String(255))
    percent = Column(Float)


t_temp_story_hotel01_location = Table(
    'temp_story_hotel01_location', metadata,
    Column('title', String(255)),
    Column('radius', Integer),
    Column('latitude', Numeric(10, 7)),
    Column('longitude', Numeric(10, 7))
)


class TempStoryStatic(Base):
    __tablename__ = 'temp_story_static'

    id = Column(BigInteger, primary_key=True)
    section_label = Column(String(64), nullable=False)
    section_json = Column(JSON)


class ZImportEDMCity01(Base):
    __tablename__ = 'z_import_EDM_City01'

    HierID = Column(BigInteger, primary_key=True)
    Region = Column(String(255))
    ShortRegion = Column(String(255))
    Continent = Column(String(255))
    ContinentCode = Column(String(255))
    Country = Column(String(255))
    CountryCode2Char = Column(String(255))
    CountryCode3Char = Column(String(255))
    CountryNumericCode = Column(String(255))
    State = Column(String(255))
    StateCode = Column(String(255))
    CityName = Column(String(255))
    CityCode = Column(String(255))
    CreateDate = Column(String(255))
    Updatedate = Column(String(255))
    Latitude = Column(Numeric(10, 7))
    Longitude = Column(Numeric(10, 7))


class ZImportEdmHotel(Base):
    __tablename__ = 'z_import_edm_hotel'

    BCDPropertyID = Column(String(255), primary_key=True)
    BrandName = Column(String(255))
    BrandCode = Column(String(255))
    MasterChainName = Column(String(255))
    MasterChainCode = Column(String(255))
    ActualPropertyName = Column(String(255))
    BCDPropertyName = Column(String(255))
    StreetAddress1 = Column(String(255))
    StreetAddress2 = Column(String(255))
    City = Column(String(255))
    StateProvinceName = Column(String(255))
    StateProvinceCode = Column(String(255))
    PostalCode = Column(String(255))
    PostalCodeLast4 = Column(String(255))
    CountryName = Column(String(255))
    CountryCode2Char = Column(String(255))
    CountryCode3Char = Column(String(255))
    CountryCodeDigit = Column(String(255))
    PropertyLatitude = Column(String(255))
    PropertyLongitude = Column(String(255))
    GeoResolutionCode = Column(String(255))
    GeoResolution = Column(String(255))
    AirportCode = Column(String(255))
    BCDMultiAirportCityCode = Column(String(255))
    BCDMultiAirportCityName = Column(String(255))
    MultiAirportCityCode = Column(String(255))
    AirportLatitude = Column(String(255))
    AirportLongitude = Column(String(255))
    DistanceMiles = Column(String(255))
    DistanceKM = Column(String(255))
    PropertyType = Column(String(255))
    Phone = Column(String(255))
    PhoneCountrycode = Column(String(255))
    PhoneCityCode = Column(String(255))
    PhoneExchange = Column(String(255))
    Fax = Column(String(255))
    FaxCountryCode = Column(String(255))
    FaxCityCode = Column(String(255))
    FaxExchange = Column(String(255))
    AmadeusID = Column(String(255))
    AmadeusBrandCode = Column(String(255))
    WorldSpanID = Column(String(255))
    WorldSpanBrandCode = Column(String(255))
    SabreID = Column(String(255))
    SabreBrandCode = Column(String(255))
    ApolloID = Column(String(255))
    ApolloBrandCode = Column(String(255))
    MarketTier = Column(String(255))
    ServiceLevel = Column(String(255))
    CreateDate = Column(String(255))
    UpdateDate = Column(String(255))
    AlternateBrandName = Column(String(255))
    RecordType = Column(String(255))


class AdvitoApplicationFeature(Base):
    __tablename__ = 'advito_application_feature'

    id = Column(BigInteger, primary_key=True)
    advito_application_id = Column(ForeignKey('advito_application.id'), nullable=False)
    feature_name = Column(String(64), nullable=False)
    feature_tag = Column(String(8), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_application = relationship('AdvitoApplication')


class AdvitoApplicationPersona(Base):
    __tablename__ = 'advito_application_persona'

    id = Column(BigInteger, primary_key=True)
    advito_application_id = Column(ForeignKey('advito_application.id'), nullable=False)
    persona_name = Column(String(32), nullable=False, index=True)
    persona_tag = Column(String(8), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False)

    advito_application = relationship('AdvitoApplication')


class AdvitoApplicationRole(Base):
    __tablename__ = 'advito_application_role'

    id = Column(BigInteger, primary_key=True)
    advito_application_id = Column(ForeignKey('advito_application.id'), nullable=False)
    role_name = Column(String(64), nullable=False)
    role_tag = Column(String(8), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)
    is_assignable = Column(Boolean, nullable=False, server_default=text("true"))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_application = relationship('AdvitoApplication')


class AdvitoUser(Base):
    __tablename__ = 'advito_user'

    id = Column(BigInteger, primary_key=True)
    client_id = Column(ForeignKey('client.id'), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    pwd = Column(String(128), nullable=False, index=True)
    name_last = Column(String(64), nullable=False, index=True)
    name_first = Column(String(64), nullable=False)
    is_enabled = Column(Boolean, nullable=False, server_default=text("false"))
    is_verified = Column(Boolean, nullable=False, server_default=text("false"))
    must_change_pwd = Column(Boolean, nullable=False, server_default=text("false"))
    pwd_expiration = Column(Date)
    email = Column(String(128), nullable=False)
    phone = Column(String(64))
    profile_picture_path = Column(String(256))
    default_timezone = Column(String(128))
    default_language = Column(String(16))
    user_salt = Column(String(64))
    default_date_format = Column(String(32))
    address = Column(String(255))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    client = relationship('Client')


class ClientDivision(Base):
    __tablename__ = 'client_division'

    id = Column(BigInteger, primary_key=True)
    client_id = Column(ForeignKey('client.id'), nullable=False)
    division_name = Column(String(32), nullable=False)
    division_name_full = Column(String(64), nullable=False)
    division_tag = Column(String(8), nullable=False)
    gcn = Column(String(16))
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    client = relationship('Client')


class GeoRegion(Base):
    __tablename__ = 'geo_region'

    id = Column(BigInteger, primary_key=True)
    geo_region_group_id = Column(ForeignKey('geo_region_group.id'), nullable=False)
    region_name = Column(String(64), nullable=False)
    region_code = Column(String(4))
    region_note = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    geo_region_group = relationship('GeoRegionGroup')


class AccessToken(Base):
    __tablename__ = 'access_token'

    id = Column(BigInteger, primary_key=True)
    advito_user_id = Column(ForeignKey('advito_user.id'), nullable=False)
    token_type = Column(String(32), nullable=False)
    token = Column(String(128), nullable=False, index=True)
    token_expiration = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_user = relationship('AdvitoUser')


class AdvitoApplicationRoleGroupLink(Base):
    __tablename__ = 'advito_application_role_group_link'

    id = Column(BigInteger, primary_key=True)
    advito_application_role_id = Column(ForeignKey('advito_application_role.id'), nullable=False)
    advito_group_id = Column(ForeignKey('advito_group.id'), nullable=False)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modifed = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_application_role = relationship('AdvitoApplicationRole')
    advito_group = relationship('AdvitoGroup')


class AdvitoUserClientunitLink(Base):
    __tablename__ = 'advito_user_clientunit_link'

    id = Column(BigInteger, primary_key=True)
    advito_user_id = Column(ForeignKey('advito_user.id'), nullable=False)
    client_unit_id = Column(ForeignKey('client_division.id'), nullable=False)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_user = relationship('AdvitoUser')
    client_unit = relationship('ClientDivision')


class AdvitoUserGroupLink(Base):
    __tablename__ = 'advito_user_group_link'

    id = Column(BigInteger, primary_key=True)
    advito_user_id = Column(ForeignKey('advito_user.id'), nullable=False)
    advito_group_id = Column(ForeignKey('advito_group.id'), nullable=False)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_group = relationship('AdvitoGroup')
    advito_user = relationship('AdvitoUser')


class AdvitoUserPersonaLink(Base):
    __tablename__ = 'advito_user_persona_link'

    id = Column(BigInteger, primary_key=True)
    advito_user_id = Column(ForeignKey('advito_user.id'), nullable=False)
    advito_application_persona_id = Column(ForeignKey('advito_application_persona.id'), nullable=False)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_application_persona = relationship('AdvitoApplicationPersona')
    advito_user = relationship('AdvitoUser')


class AdvitoUserRoleLink(Base):
    __tablename__ = 'advito_user_role_link'

    id = Column(BigInteger, primary_key=True)
    advito_user_id = Column(ForeignKey('advito_user.id'), nullable=False)
    advito_role_id = Column(ForeignKey('advito_application_role.id'), nullable=False)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_role = relationship('AdvitoApplicationRole')
    advito_user = relationship('AdvitoUser')


class AdvitoUserSession(Base):
    __tablename__ = 'advito_user_session'

    id = Column(BigInteger, primary_key=True)
    advito_user_id = Column(ForeignKey('advito_user.id'), nullable=False)
    session_token = Column(String(128), nullable=False, unique=True)
    session_start = Column(TIMESTAMP(precision=6), nullable=False)
    session_end = Column(TIMESTAMP(precision=6))
    session_duration_sec = Column(Integer)
    session_type = Column(String(32))
    session_expiration = Column(TIMESTAMP(precision=6), nullable=False)
    session_note = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_user = relationship('AdvitoUser')


class ClientFeatureLink(Base):
    __tablename__ = 'client_feature_link'

    id = Column(BigInteger, primary_key=True)
    client_id = Column(ForeignKey('client.id'), nullable=False)
    advito_application_feature_id = Column(ForeignKey('advito_application_feature.id'), nullable=False)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_application_feature = relationship('AdvitoApplicationFeature')
    client = relationship('Client')


class GeoSubregion(Base):
    __tablename__ = 'geo_subregion'

    id = Column(BigInteger, primary_key=True)
    geo_region_id = Column(ForeignKey('geo_region.id'), nullable=False)
    subregion_name = Column(String(64), nullable=False)
    subregion_code = Column(String(4))
    subregion_note = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    geo_region = relationship('GeoRegion')


class AdvitoUserSessionLog(Base):
    __tablename__ = 'advito_user_session_log'

    id = Column(BigInteger, primary_key=True)
    advito_application_id = Column(ForeignKey('advito_application.id'), nullable=False)
    session_token = Column(ForeignKey('advito_user_session.session_token'), nullable=False)
    log_timestamp = Column(DateTime, nullable=False)
    log_action = Column(String(64), nullable=False)
    log_detail = Column(String(64))
    result_code = Column(String(16))
    log_object = Column(String(64))
    log_object_id = Column(BigInteger)
    summary_json = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_application = relationship('AdvitoApplication')
    advito_user_session = relationship('AdvitoUserSession')
