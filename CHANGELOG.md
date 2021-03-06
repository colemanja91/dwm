## 2017-10-10 v1.0.2
- Fix bug preventing install in some systems

## 2017-10-05 v1.0.0
- Overhaul to new class-based implementation; we have been running it stable in PROD for about 3 months now. See docs for details. *Breaking Changes*

## 2017-01-16 v0.0.8
- Feature Change - Field `derivations` check. Add an additional boolean flag indicater if the function found a match.      
- Change hardcoded dict config values for `derive` to a list.
- Create Travis initial file for CI.
- Add requirements for travis CI.
- Update to use nosetests ( update travis yml file to run nosetests )

## 2016-12-01 v0.0.7
- Update diagrams to show `normIncludes`
- Add `_current` field to recorded history; most recent record is `0`, all other records increment in ascending order

## 2016-09-22 v0.0.6
- Removed outdated `type` fields from test records
- Added try/catch for KeyError in records returned from MongoDB
- Major: Added `normIncludes` and `deriveIncludes` functionality as an alternative to regex
  - faster in cases where looking for:
    - a set of words in string
    - a set of words not in string
    - begins with a word
    - ends with a word
  - Initial testing saw a 2x time improvement

## 2016-09-20 v0.0.5 (hotfix)
- Switched loop/conditional for DeriveDataLookupAll; before was looping by order of keys in `data`, now looping by order of fields in `config`

## 2016-09-16 v0.0.4
- Split expected MongoDB schema into collections based on the former `type` field:
  - genericLookup, genericRegex, fieldSpecificLookup, fieldSpecificRegex, normLookup, normRegex, deriveValue
- Added config-level derive option for `blankIfNoMatch`; defaults to `False`
- contactHistory now includes config name
- Added projection to MongoDB queries to only return required fields for cleaning
- Cleaned up inline function docs, added auto-generated Sphinx docs
- Finished building out DataDictionary and README
- Added ability to pass in a config to `dwmAll` in case an `OrderedDict` is required

## 2016-09-02 v0.0.3
 - Instead of sorting the "derive" and "userDefinedFunctions" config dicts at use, now sort them in the top-level function dwmAll. This means, if you're running 10 fields for 1000 contacts, instead of calling ```sorted()``` 18,000 times, you call it 18 times at the very beginning to created OrderedDict.
 - Moved all references to setting/returning record-level history into the "config" object

## 2016-08-24 v0.0.2
 - Initial release
