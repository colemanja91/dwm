""" Main class for DWM """

from .cleaning import DataLookup, RegexLookup

##########################################################################
# Constants
##########################################################################

LOOKUP_TYPES = ['genericLookup', 'genericRegex', 'fieldSpecificRegex',
                'fieldSpecificLookup', 'normLookup', 'normRegex',
                'normIncludes']

DERIVE_TYPES = ['deriveValue', 'copyValue', 'deriveRegex', 'deriveIncludes']

DERIVE_OPTIONS = ['overwrite', 'blankIfNoMatch']

UDF_POSITIONS = ['beforeGenericValLookup', 'beforeGenericValRegex',
                 'beforeFieldSpecificLookup', 'beforeFieldSpecificRegex',
                 'beforeNormLookup', 'beforeNormRegex',
                 'beforeNormIncludes', 'beforeDerive', 'afterAll']

##########################################################################
# DWM
##########################################################################


class Dwm(object):
    """ class for DWM config """

    def __init__(self, name, mongo, fields=None, udfs=None):
        """
        Set configuration for DWM runtime

        :param str name: Name of configuration; for logging
        :param MongoClient mongo: MongoDB connection
        :param list fields: list of field configurations (dict)
        :param dict udfs: dict of udfs to run
        """

        if fields is None:
            fields = []

        if udfs is None:
            udfs = {}

        # validate input values
        for field in fields:
            # lookup values
            for lookup in fields[field]['lookup']:
                if lookup not in LOOKUP_TYPES:
                    raise ValueError('Invalid lookup type %s' % lookup)

            # derive types and options
            for derive in fields[field]['derive']:
                if derive['type'] not in DERIVE_TYPES:
                    raise ValueError('Invalid derive type %s' % derive['type'])

                for opt in derive['options']:
                    if opt not in DERIVE_OPTIONS:
                        raise ValueError('Invalid derive option %s' % opt)

        for udf in udfs:
            if udf not in UDF_POSITIONS:
                raise ValueError('Invalid UDF position %s' % udf)

        self.name = name
        self.mongo = mongo
        self.fields = fields
        self.udfs = udfs

    def _val_g_lookup(self, record, hist=None):
        """
        Perform generic validation lookup

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """
        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:

                    if 'genericLookup' in self.fields[field]['lookup']:

                        field_val_new, hist = DataLookup(fieldVal=record[field],
                                                         db=self.mongo,
                                                         lookupType='genericLookup',
                                                         fieldName=field,
                                                         histObj=hist)

                        record[field] = field_val_new

        return record, hist

    def _val_g_regex(self, record, hist=None):
        """
        Perform generic validation regex

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """
        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:

                    if 'genericRegex' in self.fields[field]['lookup']:

                        field_val_new, hist = RegexLookup(fieldVal=record[field],
                                                          db=self.mongo,
                                                          fieldName=field,
                                                          lookupType='genericRegex',
                                                          histObj=hist)

                        record[field] = field_val_new

        return record, hist

    def _val_fs_lookup(self, record, hist=None):
        """
        Perform field-specific validation lookup

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """
        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:

                    if 'fieldSpecificLookup' in self.fields[field]['lookup']:

                        field_val_new, hist = DataLookup(fieldVal=record[field],
                                                         db=self.mongo,
                                                         lookupType='fieldSpecificLookup',
                                                         fieldName=field,
                                                         histObj=hist)

                        record[field] = field_val_new

        return record, hist

    def _val_fs_regex(self, record, hist=None):
        """
        Perform field-specific validation regex

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """

        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:

                    if 'fieldSpecificRegex' in self.fields[field]['lookup']:

                        field_val_new, hist = RegexLookup(fieldVal=record[field],
                                                          db=self.mongo,
                                                          fieldName=field,
                                                          lookupType='fieldSpecificRegex',
                                                          histObj=hist)
                        print(field_val_new)
                        print(hist)
                        record[field] = field_val_new

        return record, hist

    def _norm_lookup(self, record, hist=None):
        """
        Perform generic validation lookup

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """
        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:

                    if 'normLookup' in self.fields[field]['lookup']:
                        field_val_new, hist = DataLookup(fieldVal=record[field],
                                                         db=self.mongo,
                                                         lookupType='normLookup',
                                                         fieldName=field,
                                                         histObj=hist)

                        record[field] = field_val_new

        return record, hist

    def _norm_regex(self, record, hist=None):
        """
        Perform generic validation regex

        :param dict record: dictionary of values to validate
        :param dict hist: existing input of history values
        """
        if hist is None:
            hist = {}

        for field in record:

            if record[field] != '' and record[field] is not None:

                if field in self.fields:

                    if 'normRegex' in self.fields[field]['lookup']:
                        field_val_new, hist = RegexLookup(fieldVal=record[field],
                                                          db=self.mongo,
                                                          fieldName=field,
                                                          lookupType='normRegex',
                                                          histObj=hist)

                        record[field] = field_val_new

        return record, hist
