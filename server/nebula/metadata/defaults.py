from ..common import config
from ..constants import *

DEFAULT_META_TYPES = {
# KEY                      "o", I  F  CLASS        SETTINGS
"id":                     ("o", 1, 0, INTEGER,     {}),
"ctime":                  ("o", 1, 0, DATETIME,    {}),              # Creation time
"mtime":                  ("o", 1, 0, DATETIME,    {}),              # Last modified time
"mark_in":                ("e", 1, 0, TIMECODE,    {}),
"mark_out":               ("e", 1, 0, TIMECODE,    {}),
"logo":                   ("e", 1, 0, SELECT,      {"cs" : "urn:site:logo"}),
"media_type":             ("o", 1, 0, INTEGER,     {}),
"content_type":           ("o", 1, 0, INTEGER,     {}),
"status":                 ("o", 1, 0, INTEGER,     {"default" : 1}),              # OFFLINE, ONLINE, CREATING, TRASHED, ARCHIVED
"id_storage":             ("o", 1, 0, INTEGER,     {}),
"id_folder":              ("m", 1, 0, INTEGER,     {}),
"path":                   ("o", 1, 1, STRING,      {}),
"subclips":               ("o", 0, 0, OBJECT,      {}),
"article":                ("m", 1, 6, TEXT,        {"mode" : "rich"}),
"cue_sheet":              ("m", 1, 1, TEXT,        {}),
"aired":                  ("e", 1, 0, BOOLEAN,     {}),
"title":                  ("m", 1, 9, STRING,      {}),                       # dc.title.main - The title most commonly associated with the resource.
"subtitle":               ("m", 1, 8, STRING,      {}),                       # dc.title.subtitle - Ancillary title information for the resource.
"description":            ("m", 1, 7, TEXT,        {"mode" : "rich"}),
"color":                  ("m", 0, 0, INTEGER,     {}),                       # Object highlight color
"notes":                  ("m", 1, 1, TEXT,        {}),                       # Production notes
"promoted":               ("m", 1, 0, BOOLEAN,     {}),                       # Asset "promotion". It"s hit, important, favourite,....
"language":               ("m", 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:ISO639_1LanguageCodeCS", "order" : "alias"}),
"editorial_format":       ("m", 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:EditorialFormatCodeCS", "mode" : "tree"}),
"editorial_control":      ("m", 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:EditorialControlCodeCS", "mode" : "radio"}),
"intended_audience":      ("m", 1, 0, LIST,        {"cs" : "urn:ebu:metadata-cs:IntendedAudienceCodeCS", "mode" : "tree"}),
"intention":              ("m", 1, 0, LIST,        {"cs" : "urn:ebu:metadata-cs:IntentionCodeCS", "mode" : "tree"}),
"genre":                  ("m", 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:ContentGenreCS", "mode" : "tree"}),
"atmosphere":             ("m", 1, 0, LIST,        {"cs" : "urn:tva:metadata-cs:AtmosphereCS", "order" : "alias"}),
"place":                  ("m", 1, 0, LIST,        {"cs" : "urn:tva:metadata-cs:PlaceTypeCS", "mode" : "tree"}),
"origination":            ("m", 1, 0, SELECT,      {"cs" : "urn:tva:metadata:cs:OriginationCS", "mode" : "tree"}),
"content_alert":          ("m", 1, 0, LIST,        {"cs" : "urn:tva:metadata-cs:ContentAlertCS", "mode" : "tree"}),
"content_alert/scheme":   ("m", 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:ContentAlertSchemeCodeCS", "mode" : "tree"}),
"graphic_usage":          ("m", 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:GraphicUsageTypeCodeCS"}),
"keywords":               ("m", 1, 9, STRING,      {}),                       # Comma delimited keywords list
"year":                   ("m", 1, 0, INTEGER,     {"hide_null" : True}),
"date":                   ("m", 1, 0, DATETIME,    {"mode" : "date"}),
"date/valid":             ("m", 1, 0, DATETIME,    {"mode" : "date"}),
"date/valid/ott":         ("m", 1, 0, DATETIME,    {"mode" : "date"}),
"rights":                 ("m", 1, 0, SELECT,      {"cs" : "urn:immstudios:metadata-cs:ContentLicenceCS"}),
"rights/type":            ("m", 1, 0, LIST,        {"cs" : "urn:ebu:metadata-cs:RightTypeCodeCS"}),
"rights/attribution":     ("m", 1, 1, STRING,      {}),
"rights/attribution/url": ("m", 1, 1, STRING,      {}),
"rights/description":     ("m", 1, 1, TEXT,        {}),
"rights/ott":             ("m", 1, 0, BOOLEAN,     {}),
"rights/spatial":         ("m", 1, 0, SELECT,      {"cs" : "urn:site:rights-spatial"}),
"source":                 ("m", 1, 1, STRING,      {}),                       # Youtube, Vimeo, PirateBay....
"source/url":             ("m", 1, 1, STRING,      {}),
"source/attribution":     ("m", 1, 1, STRING,      {}),                       # DEPRECATED
"source/rating":          ("m", 1, 0, INTEGER,     {}),                       # Provided rating normalized to: from 0 (worst) to 100 (best)
"commercial/content":     ("m", 1, 0, SELECT,      {"cs" : "urn:tva:metadata-cs:ContentCommercialCS", "mode" : "tree"}),
"commercial/campaign":    ("m", 1, 0, INTEGER,     {}),                       # Campaign event id
"commercial/client":      ("m", 1, 0, SELECT,      {"cs" : "urn:site:clients"}),
"runs/daily":             ("m", 0, 0, INTEGER,     {}),
"runs/weekly":            ("m", 0, 0, INTEGER,     {}),
"runs/monthly":           ("m", 0, 0, INTEGER,     {}),
"runs/total":             ("m", 0, 0, INTEGER,     {}),
"album":                  ("m", 1, 5, STRING,      {}),
"serie":                  ("m", 1, 0, SELECT,      {"cs" : "urn:site:series", "order" : "alias"}),
"serie/season":           ("m", 1, 0, INTEGER,     {}),
"serie/episode":          ("m", 1, 0, INTEGER,     {}),
"id/main":                ("m", 1, 8, STRING,      {}),                       # Primary Content ID (local or global)
"id/youtube":             ("m", 1, 8, STRING,      {}),                       # Youtube ID if exists
"id/vimeo":               ("m", 1, 8, STRING,      {}),                       # Vimeo ID if exists
"id/imdb":                ("m", 1, 8, STRING,      {}),                       # IMDB ID for movies
"id/guid":                ("m", 1, 8, STRING,      {}),                       # Created automatically when asset is created
"id/vod":                 ("m", 1, 8, STRING,      {}),                       # VOD KEY
"id/tape":                ("m", 1, 8, STRING,      {}),                       # Archive tape ID
"id/umid":                ("m", 1, 8, STRING,      {}),
"role/director":          ("m", 1, 7, STRING,      {}),
"role/performer":         ("m", 1, 7, STRING,      {}),
"role/composer":          ("m", 1, 7, STRING,      {}),
"role/cast":              ("m", 1, 7, STRING,      {}),              # Coma delimited cast
"duration":               ("f", 1, 0, TIMECODE,    {}),              # Clip duration.
"start_timecode":         ("f", 1, 0, TIMECODE,    {}),
"file/mtime":             ("f", 1, 0, DATETIME,    {}),              # Timestamp of file last modification
"file/size":              ("f", 1, 0, INTEGER,     {}),              # File size in bytes
"file/format":            ("f", 1, 0, STRING,      {}),              # Container format name. from ffprobe/format/format_name
"video/index":            ("f", 0, 0, INTEGER,     {}),              # Index of the video track
"video/width":            ("f", 0, 0, INTEGER,     {}),              # Video frame / image width (pixels)
"video/height":           ("f", 0, 0, INTEGER,     {}),              # Video frame / image height (pixels)
"video/fps":              ("f", 0, 0, FRACTION,    {}),
"video/fps_f":            ("f", 0, 0, NUMERIC,     {}),
"video/pixel_format":     ("f", 0, 0, STRING,      {}),
"video/color_range":      ("f", 0, 0, STRING,      {}),
"video/color_space":      ("f", 0, 0, STRING,      {}),
"video/aspect_ratio":     ("f", 0, 0, FRACTION,    {}),
"video/aspect_ratio_f":   ("f", 0, 0, NUMERIC,     {}),
"video/codec":            ("f", 0, 0, STRING,      {}),
"video/display_format":   ("f", 1, 0, SELECT,      {"cs" : "urn:ebu:metadata-cs:PictureDisplayFormatCodeCS"}),
"video/is_interlaced":    ("f", 0, 0, BOOLEAN,     {}),
"qc/state":               ("q", 1, 0, INTEGER,     {}),              # Special widget 1 and 2 are reserved for Auto QC failed and passed states
"qc/report":              ("q", 1, 1, TEXT,        {}),              # Holds error report from QC Pass and/or rejection/approval message from QC humanoid
"audio/bpm":              ("q", 1, 0, NUMERIC,     {}),              # Music BPM
"audio/r128/i":           ("q", 0, 0, NUMERIC,     {}),              # Integrated loudness (LUFS)
"audio/r128/t":           ("q", 0, 0, NUMERIC,     {}),              # Integrated loudness threshold (LUFS)
"audio/r128/lra":         ("q", 0, 0, NUMERIC,     {}),              # LRA (LU)
"audio/r128/lra/t":       ("q", 0, 0, NUMERIC,     {}),              # Loudness range threshold (LUFS)
"audio/r128/lra/l":       ("q", 0, 0, NUMERIC,     {}),              # LRA Low (LUFS)
"audio/r128/lra/r":       ("q", 0, 0, NUMERIC,     {}),              # LRA High (LUFS)
"audio/gain/mean":        ("q", 0, 0, NUMERIC,     {}),
"audio/gain/peak":        ("q", 0, 0, NUMERIC,     {}),
"audio/silence":          ("q", 0, 0, OBJECT,      {}),              # Areas with silent audio
"audio/clipping":         ("q", 0, 0, OBJECT,      {}),              # Audio clipping areas
"video/black":            ("q", 0, 0, OBJECT,      {}),              # Areas where video is black-only
"video/static":           ("q", 0, 0, OBJECT,      {}),              # Areas with static image
}


 
DEFAULT_ALIASES = [
  ["commercial/content"     , "Commercial content"     , "Content"           , ""],
  ["solver"                 , "Solver"                 , None                , ""],
  ["year"                   , "Year"                   , None                , ""],
  ["id_user"                , "User ID"                , None                , ""],
  ["audio/r128/i"           , "Integrated loudness"    , "LUFS"              , ""],
  ["rundown_row"            , ""                       , ""                  , ""],
  ["video/pixel_format"     , "Pixel format"           , None                , ""],
  ["subtitle"               , "Subtitle"               , None                , "The title and subtitle should together make a full title"],
  ["editorial_control"      , "Editorial control"      , "Control"           , ""],
  ["full_name"              , "Full name"              , None                , ""],
  ["origination"            , "Origination"            , None                , ""],
  ["start"                  , "Start"                  , None                , ""],
  ["album"                  , "Album"                  , None                , ""],
  ["file/mtime"             , "File modified"          , "File time"         , ""],
  ["duration"               , "Duration"               , None                , ""],
  ["article"                , "Article"                , None                , ""],
  ["video/fps"              , "FPS"                    , None                , ""],
  ["content_alert"          , "Content alert"          , None                , ""],
  ["video/fps_f"            , "FPS"                    , None                , ""],
  ["aired"                  , "Aired"                  , None                , ""],
  ["qc/report"              , "QC report"              , None                , ""],
  ["path"                   , "Path"                   , None                , ""],
  ["stop"                   , "Stop"                   , None                , ""],
  ["id_asset"               , "Asset ID"               , None                , ""],
  ["runs/total"             , "Runs total"             , "Runs"              , ""],
  ["audio/codec"            , "Audio codec"            , None                , ""],
  ["role/composer"          , "Composer"               , None                , "Coma delimited list of composers"],
  ["cue_sheet"              , "Cue sheet"              , None                , ""],
  ["notes"                  , "Notes"                  , None                , ""],
  ["ctime"                  , "Creation time"          , "Created"           , "Time when the asset was created"],
  ["role/performer"         , "Artist"                 , None                , ""],
  ["source/url"             , "Source URL"             , None                , ""],
  ["subclips"               , "Subclips"               , None                , ""],
  ["rundown_symbol"         , "Rundown symbol"         , ""                  , ""],
  ["rights/type"            , "Rights type"            , None                , ""],
  ["rights/description"     , "Rights description"     , "Rights desc."      , "A legal document giving official permission to do something with the resource"],
  ["runs/weekly"            , "Runs per week"          , "Runs weelky"       , ""],
  ["video/color_space"      , "Color space"            , None                , "Video color space"],
  ["id/vimeo"               , "Vimeo ID"               , None                , ""],
  ["rundown_difference"     , "Difference"             , None                , "Difference between rundown scheduled and broadcast times"],
  ["runs/monthly"           , "Runs per month"         , "Runs monthly"      , ""],
  ["date/valid/ott"         , "OTT validity ends"      , "OTT Validity"      , ""],
  ["content_type"           , "Content type"           , None                , ""],
  ["id/guid"                , "GUID"                   , None                , ""],
  ["id/umid"                , "UMID"                   , None                , ""],
  ["serie/episode"          , "Episode"                , None                , "Episode in a specific season of a TV or video series this asset is a member of"],
  ["video/display_format"   , "Display format"         , "Disp. format"      , ""],
  ["intended_audience"      , "Intended audience"      , "Audience"          , "A class of entity for whom the resource is intended or useful"],
  ["audio/r128/lra/r"       , "LRA R"                  , None                , ""],
  ["id/vod"                 , "VOD ID"                 , None                , ""],
  ["video/aspect_ratio"     , "Aspect ratio"           , None                , ""],
  ["promoted"               , "Promoted"               , ""                  , ""],
  ["start_timecode"         , "Start TC"               , None                , ""],
  ["role/director"          , "Director"               , None                , ""],
  ["audio/r128/t"           , "audio/r128/t"           , "audio/r128/t"      , ""],
  ["audio/r128/lra"         , "LRA"                    , None                , ""],
  ["date/valid"             , "Validity ends"          , "Validity"          , "End time until when asset can be published"],
  ["genre"                  , "Genre"                  , None                , "Artistic, style, journalistic, product or other genre of the asset"],
  ["audio/bpm"              , "BPM"                    , None                , ""],
  ["intention"              , "Intention"              , None                , "The primary apparent intention in transmitting the programme"],
  ["keywords"               , "Keywords"               , None                , "Comma delimited keywords list "],
  ["color"                  , "Color"                  , None                , ""],
  ["version_of"             , "Version of"             , None                , ""],
  ["rights"                 , "Rights"                 , None                , ""],
  ["rundown_scheduled"      , "Scheduled time"         , "Scheduled"         , ""],
  ["id/tape"                , "Tape ID"                , None                , ""],
  ["graphic_usage"          , "Graphic usage"          , "Usage"             , ""],
  ["audio/silence"          , "Silence"                , None                , ""],
  ["place"                  , "Place"                  , None                , ""],
  ["video/is_interlaced"    , "Is interlaced"          , "Interlaced"        , ""],
  ["id_item"                , "Item ID"                , None                , ""],
  ["rights/spatial"         , "Spatial rights"         , None                , ""],
  ["source/attribution"     , "Attribution"            , None                , "Credit to person(s) and/or organisation(s) required by the supplier of the asset to be used when published."],
  ["rundown_broadcast"      , "Broadcast time"         , "Broadcast"         , ""],
  ["serie"                  , "Serie"                  , None                , "TV or video series this asset is a member of"],
  ["video/static"           , "Static"                 , "Static"            , ""],
  ["file/size"              , "File size"              , "Size"              , ""],
  ["rights/attribution/url" , "Attribution URL"        , None                , ""],
  ["qc/state"               , "QC state"               , ""                  , ""],
  ["source/rating"          , "Rating"                 , None                , ""],
  ["video/width"            , "Width"                  , None                , ""],
  ["logo"                   , "Logo"                   , None                , ""],
  ["status"                 , "Status"                 , None                , ""],
  ["rights/ott"             , "OTT Rights"             , "OTT"               , ""],
  ["id_event"               , "Event ID"               , None                , ""],
  ["id_bin"                 , "Bin ID"                 , None                , ""],
  ["role/cast"              , "Cast"                   , None                , "Coma delimited list of actors"],
  ["source"                 , "Source"                 , None                , ""],
  ["id_folder"              , "Folder"                 , None                , ""],
  ["is_admin"               , "Admin"                  , None                , ""],
  ["run_mode"               , "Run mode"               , None                , ""],
  ["description"            , "Description"            , None                , ""],
  ["file/format"            , "File format"            , None                , ""],
  ["id"                     , "ID"                     , "#"                 , ""],
  ["id/imdb"                , "IMDB ID"                , None                , ""],
  ["audio/clipping"         , "Clipping"               , None                , ""],
  ["id/youtube"             , "Youtube ID"             , None                , ""],
  ["audio/gain/mean"        , "Mean audio gain"        , "Mean gain"         , ""],
  ["mtime"                  , "Modify time"            , "Modified"          , "Time when the asset was modified last time"],
  ["media_type"             , "Media type"             , None                , ""],
  ["rights/attribution"     , "Attribution"            , None                , ""],
  ["video/color_range"      , "Color range"            , None                , ""],
  ["video/black"            , "Black"                  , None                , ""],
  ["video/aspect_ratio_f"   , "Aspect ratio"           , "Aspect"            , ""],
  ["atmosphere"             , "Atmosphere"             , None                , "Feeling summarising the atmosphere"],
  ["video/index"            , "Video track index"      , "Video index"       , ""],
  ["video/height"           , "Height"                 , None                , ""],
  ["mark_out"               , "Mark out"               , None                , "The point in time the content proposed for editorial use starts"],
  ["description/original"   , "Original description"   , "Orig. description" , ""],
  ["language"               , "Language"               , None                , "Language version of the asset"],
  ["audio/r128/lra/t"       , "LRA T"                  , None                , ""],
  ["date"                   , "Date"                   , None                , ""],
  ["title"                  , "Title"                  , None                , "The title most commonly associated with the resource"],
  ["audio/r128/lra/l"       , "LRA L"                  , None                , ""],
  ["id/main"                , "IDEC"                   , None                , "An unambiguous reference to the resource within a given context"],
  ["subtitle/original"      , "Original subtitle"      , "Orig. subtitle"    , ""],
  ["mark_in"                , "Mark in"                , "In"                , "The point in time the content proposed for editorial use ends"],
  ["commercial/client"      , "Client"                 , None                , ""],
  ["title/original"         , "Original title"         , "Orig. title"       , ""],
  ["id_storage"             , "Storage"                , None                , ""],
  ["editorial_format"       , "Format"                 , None                , "Programme formal structure: how does the programme look, regardless of the subject with which the programme is dealing"],
  ["is_empty"               , ""                       , ""                  , ""],
  ["commercial/campaign"    , "Campaign"               , None                , ""],
  ["runs/daily"             , "Runs per day"           , "Runs daily"        , ""],
  ["serie/season"           , "Season"                 , None                , "Season of a TV or video series this asset is a member of"],
  ["content_alert/scheme"   , "Content alert scheme"   , "PG"                , "Information about a particular type of content potentially sensitive"],
  ["video/codec"            , "Video codec"            , None                , ""],
  ["audio/gain/peak"        , "Audio peak"             , None                , ""]
]


for key in DEFAULT_META_TYPES:
    d = DEFAULT_META_TYPES[key]
    config["meta_types"][key] = {
        "ns" : d[0],
        "index" : d[1],
        "fulltext" : d[2] if d[1] else 0,
        "class" : d[3],
    **d[4]}

for key, alias, col_header, description in DEFAULT_ALIASES:
    if not key in config["meta_types"]:
        continue

    config["meta_types"][key]["alias"] = {"en" : alias}
    if col_header is not None:
        config["meta_types"][key]["col_header"] = {"en" : col_header}
    if description:
        config["meta_types"][key]["description"] = {"en" : description}