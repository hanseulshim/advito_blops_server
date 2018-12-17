# coding: utf-8
from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, UniqueConstraint, text
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


class Client(Base):
    __tablename__ = 'client'

    id = Column(BigInteger, primary_key=True)
    client_name = Column(String(32), nullable=False)
    client_name_full = Column(String(64), nullable=False)
    client_tag = Column(String(8), nullable=False)
    client_code = Column(String(8), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    logo_path = Column(String(128))
    description = Column(Text)
    industry = Column(String(64))
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))


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
    must_change_pwd = Column(Boolean, nullable=False, server_default=text("false"))
    pwd_expiration = Column(Date)
    email = Column(String(128), nullable=False)
    phone = Column(String(32))
    profile_picture_path = Column(String(128))
    timezone_default = Column(String(128))
    language_default = Column(String(16))
    user_salt = Column(String(64))
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
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    client = relationship('Client')


class GeoState(Base):
    __tablename__ = 'geo_state'

    id = Column(BigInteger, primary_key=True)
    geo_country_id = Column(ForeignKey('geo_country.id'), nullable=False)
    state = Column(String(64), nullable=False)
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


class AdvitoUserSessionLog(Base):
    __tablename__ = 'advito_user_session_log'

    id = Column(BigInteger, primary_key=True)
    session_token = Column(ForeignKey('advito_user_session.session_token'), nullable=False)
    log_timestamp = Column(DateTime, nullable=False)
    log_action = Column(String(64), nullable=False)
    log_detail = Column(String(64))
    log_result_code = Column(String(16))
    log_summary_json = Column(Text)
    created = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))
    modified = Column(TIMESTAMP(precision=6), nullable=False, server_default=text("now()"))

    advito_user_session = relationship('AdvitoUserSession')
