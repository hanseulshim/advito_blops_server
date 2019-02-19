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


class Agency(Base):
    __tablename__ = 'agency'

    id = Column(BigInteger, primary_key=True)
    agency_name = Column(String(32), nullable=False, index=True)
    agency_name_full = Column(String(64), nullable=False)
    agency_tag = Column(String(8), nullable=False)
    agency_identifier = Column(String(32), index=True)
    agency_code = Column(String(32), index=True)
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    note = Column(Text)
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
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


t_edm_airport = Table(
    'edm_airport', metadata,
    Column('loc', String(255)),
    Column('multicty', String(255)),
    Column('apt', String(255)),
    Column('type', String(255)),
    Column('subtype', String(255)),
    Column('name', String(255)),
    Column('ctry', String(255)),
    Column('subctry', String(255)),
    Column('ctryname', String(255)),
    Column('state', String(255)),
    Column('substate', String(255)),
    Column('statename', String(255)),
    Column('timediv', String(255)),
    Column('lat', String(255)),
    Column('long', String(255)),
    Column('inactive', String(255)),
    Column('gmt', String(255)),
    Column('dst', String(255)),
    Column('dststttime', String(255)),
    Column('sttdate', String(255)),
    Column('dststtstts', String(255)),
    Column('dstendtime', String(255)),
    Column('enddate', String(255)),
    Column('dstendstts', String(255)),
    Column('dstno', String(255)),
    Column('gmt02', String(255)),
    Column('time02', String(255)),
    Column('date02', String(255)),
    Column('kind02', String(255)),
    Column('time03', String(255)),
    Column('date03', String(255)),
    Column('k_ind03', String(255)),
    Column('num03', String(255)),
    Column('gmt03', String(255)),
    Column('time04', String(255)),
    Column('date04', String(255)),
    Column('k_ind04', String(255)),
    Column('time05', String(255)),
    Column('date05', String(255)),
    Column('rest', String(255))
)


t_edm_hotel = Table(
    'edm_hotel', metadata,
    Column('BCDPropertyId', String(255)),
    Column('BrandName', String(255)),
    Column('BrandCode', String(255)),
    Column('MasterChainName', String(255)),
    Column('MasterChainCode', String(255)),
    Column('ActualPropertyName', String(255)),
    Column('BCDPropertyName', String(255)),
    Column('StreetAddress1', String(255)),
    Column('StreetAddress2', String(255)),
    Column('City', String(255)),
    Column('StateProvinceName', String(255)),
    Column('StateProvinceCode', String(255)),
    Column('PostalCode', String(255)),
    Column('PostalCodeLast4', String(255)),
    Column('CountryName', String(255)),
    Column('CountryCode2Char', String(255)),
    Column('CountryCode3Char', String(255)),
    Column('CountryCodeDigit', String(255)),
    Column('PropertyLatitude', String(255)),
    Column('PropertyLongitude', String(255)),
    Column('GeoResolutionCode', String(255)),
    Column('GeoResolution', String(255)),
    Column('AirportCode', String(255)),
    Column('BCDMultAptCityCode', String(255)),
    Column('BCDMultAptCityName', String(255)),
    Column('MutiAptCityCode', String(255)),
    Column('AirportLatitude', String(255)),
    Column('AirportLongitude', String(255)),
    Column('DstMiles', String(255)),
    Column('DstKm', String(255)),
    Column('PropApTyp', String(255)),
    Column('Phone', String(255)),
    Column('PhoneCountrycode', String(255)),
    Column('PhoneCityCode', String(255)),
    Column('PhoneExchange', String(255)),
    Column('Fax', String(255)),
    Column('FaxCountryCode', String(255)),
    Column('FaxCityCode', String(255)),
    Column('FaxExchange', String(255)),
    Column('AmadeusID', String(255)),
    Column('AmadeusBrandCode', String(255)),
    Column('WorldSpanID', String(255)),
    Column('WorldSpanBrandCode', String(255)),
    Column('SabreID', String(255)),
    Column('SabreBrandCode', String(255)),
    Column('ApolloID', String(255)),
    Column('ApolloBrandCode', String(255)),
    Column('MarketTier', String(255)),
    Column('ServiceLevel', String(255))
)


t_edm_locations = Table(
    'edm_locations', metadata,
    Column('HierId', String(255)),
    Column('ContinentName', String(255)),
    Column('ContinentCode', String(255)),
    Column('Country', String(255)),
    Column('CountryCode2Letter', String(255)),
    Column('CountryCode3Letter', String(255)),
    Column('State', String(255)),
    Column('CityName', String(255))
)


class GeoCountry(Base):
    __tablename__ = 'geo_country'

    id = Column(BigInteger, primary_key=True)
    country_name = Column(String(32), nullable=False)
    country_name_full = Column(String(64), nullable=False)
    country_code = Column(String(8), nullable=False, unique=True)
    note = Column(Text)
    subdivision_label = Column(String(32))
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))
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


t_v_city = Table(
    'v_city', metadata,
    Column('geo_city_id', BigInteger),
    Column('geo_country_id', BigInteger),
    Column('country_name', String(32)),
    Column('geo_state_id', BigInteger),
    Column('state_name', String(64)),
    Column('city_name', String(128)),
    Column('city_code', String(8)),
    Column('latitude', Numeric(10, 7)),
    Column('longitude', Numeric(10, 7))
)


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


class ClientUnit(Base):
    __tablename__ = 'client_unit'

    id = Column(BigInteger, primary_key=True)
    client_id = Column(ForeignKey('client.id'), nullable=False)
    unit_name = Column(String(32), nullable=False)
    unit_name_full = Column(String(64), nullable=False)
    unit_tag = Column(String(8), nullable=False)
    gcn = Column(String(16))
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    client = relationship('Client')


class GeoState(Base):
    __tablename__ = 'geo_state'

    id = Column(BigInteger, primary_key=True)
    geo_country_id = Column(ForeignKey('geo_country.id'), nullable=False)
    state_name = Column(String(64), nullable=False)
    state_code = Column(String(8), nullable=False)
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    geo_country = relationship('GeoCountry')


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
    client_unit_id = Column(ForeignKey('client_unit.id'), nullable=False)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_user = relationship('AdvitoUser')
    client_unit = relationship('ClientUnit')


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


class GeoCity(Base):
    __tablename__ = 'geo_city'

    id = Column(BigInteger, primary_key=True)
    geo_country_id = Column(ForeignKey('geo_country.id'))
    geo_state_id = Column(ForeignKey('geo_state.id'))
    city_name = Column(String(128), nullable=False, index=True)
    city_code = Column(String(8))
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    geo_country = relationship('GeoCountry')
    geo_state = relationship('GeoState')


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


class Airport(Base):
    __tablename__ = 'airport'

    id = Column(BigInteger, primary_key=True)
    airport_name = Column(String(64), nullable=False)
    airport_code = Column(String(8), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    airport_type = Column(String(32))
    note = Column(Text)
    address1 = Column(String(64))
    address2 = Column(String(64))
    geo_city_id = Column(ForeignKey('geo_city.id'), nullable=False)
    geo_state_id = Column(ForeignKey('geo_state.id'))
    geo_country_id = Column(ForeignKey('geo_country.id'), nullable=False)
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))
    region_code = Column(String(8))
    subregion_code = Column(String(8))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    geo_city = relationship('GeoCity')
    geo_country = relationship('GeoCountry')
    geo_state = relationship('GeoState')
