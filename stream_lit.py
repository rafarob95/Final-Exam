import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 
# Add Title
st.title("Use Pygwalker In Streamlit")
 
# Import your data
rental_sales = pd.read_csv('Cleaned Data/state_rentals_with_coordinates.csv')

# Paste the copied Pygwalker chart code here
vis_spec = """[
  {
    "config": {
      "defaultAggregated": true,
      "geoms": [
        "poi"
      ],
      "coordSystem": "geographic",
      "limit": -1,
      "timezoneDisplayOffset": 0
    },
    "encodings": {
      "dimensions": [
        {
          "dragId": "gw_dOue",
          "fid": "Region Name",
          "name": "Region Name",
          "basename": "Region Name",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_C3og",
          "fid": "Region Type",
          "name": "Region Type",
          "basename": "Region Type",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_Z_gj",
          "fid": "State Name",
          "name": "State Name",
          "basename": "State Name",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_KZ6B",
          "fid": "Date Recorded",
          "name": "Date Recorded",
          "basename": "Date Recorded",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_hpco",
          "fid": "Coordinates",
          "name": "Coordinates",
          "basename": "Coordinates",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_ngIl",
          "fid": "Latitude",
          "name": "Latitude",
          "basename": "Latitude",
          "semanticType": "quantitative",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_Zf19",
          "fid": "Longitude",
          "name": "Longitude",
          "basename": "Longitude",
          "semanticType": "quantitative",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_mea_key_fid",
          "fid": "gw_mea_key_fid",
          "name": "Measure names",
          "analyticType": "dimension",
          "semanticType": "nominal"
        }
      ],
      "measures": [
        {
          "dragId": "gw_MYF3",
          "fid": "RegionID",
          "name": "RegionID",
          "basename": "RegionID",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum",
          "offset": 0
        },
        {
          "dragId": "gw_-Y8K",
          "fid": "SizeRank",
          "name": "SizeRank",
          "basename": "SizeRank",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum",
          "offset": 0
        },
        {
          "dragId": "gw_r6fq",
          "fid": "Monthly Rent",
          "name": "Monthly Rent",
          "basename": "Monthly Rent",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum",
          "offset": 0
        },
        {
          "dragId": "gw_count_fid",
          "fid": "gw_count_fid",
          "name": "Row count",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum",
          "computed": true,
          "expression": {
            "op": "one",
            "params": [],
            "as": "gw_count_fid"
          }
        },
        {
          "dragId": "gw_mea_val_fid",
          "fid": "gw_mea_val_fid",
          "name": "Measure values",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum"
        }
      ],
      "rows": [],
      "columns": [],
      "color": [
        {
          "dragId": "gw_nFfb",
          "fid": "Monthly Rent",
          "name": "Monthly Rent",
          "basename": "Monthly Rent",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "mean",
          "offset": 0
        }
      ],
      "opacity": [],
      "size": [
        {
          "dragId": "gw_gdUr",
          "fid": "Monthly Rent",
          "name": "Monthly Rent",
          "basename": "Monthly Rent",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "mean",
          "offset": 0
        }
      ],
      "shape": [],
      "radius": [],
      "theta": [],
      "longitude": [
        {
          "dragId": "gw_EXfj",
          "fid": "Longitude",
          "name": "Longitude",
          "basename": "Longitude",
          "semanticType": "quantitative",
          "analyticType": "dimension",
          "offset": 0
        }
      ],
      "latitude": [
        {
          "dragId": "gw_lgVz",
          "fid": "Latitude",
          "name": "Latitude",
          "basename": "Latitude",
          "semanticType": "quantitative",
          "analyticType": "dimension",
          "offset": 0
        }
      ],
      "geoId": [],
      "details": [
        {
          "dragId": "gw_qtvl",
          "fid": "Date Recorded",
          "name": "Date Recorded",
          "basename": "Date Recorded",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_Xulw",
          "fid": "State Name",
          "name": "State Name",
          "basename": "State Name",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        }
      ],
      "filters": [],
      "text": []
    },
    "layout": {
      "showActions": false,
      "showTableSummary": false,
      "stack": "stack",
      "interactiveScale": false,
      "zeroScale": true,
      "background": "",
      "size": {
        "mode": "auto",
        "width": 800,
        "height": 600
      },
      "format": {},
      "geoKey": "name",
      "resolve": {
        "x": false,
        "y": false,
        "color": false,
        "opacity": false,
        "shape": false,
        "size": false
      },
      "scaleIncludeUnmatchedChoropleth": false,
      "colorPalette": "reds",
      "useSvg": false,
      "scale": {
        "opacity": {},
        "size": {}
      },
      "geoMapTileUrl": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    },
    "visId": "gw_LtRJ",
    "name": "Chart 1"
  }
]"""
 
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(rental_sales, spec=vis_spec)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)