import streamlit as st

from streamlit_calendar import calendar


events = [
    {
        "title": "Actividad 1",
        "color": "#FF6C6C",
        "start": "2025-04-21",
        "end": "2025-04-21",
        "resourceId": "JZ",
    },
    {
        "title": "Actividad 2",
        "color": "#FFBD45",
        "start": "2025-04-21",
        "end": "2025-04-21",
        "resourceId": "JG",
    },
    {
        "title": "Actividad 3",
        "color": "#FF4B4B",
        "start": "2025-04-21",
        "end": "2025-04-21",
        "resourceId": "CF",
    },
    {
        "title": "Actividad 4",
        "color": "#FF6C6C",
        "start": "2025-04-21",
        "end": "2025-04-21",
        "resourceId": "JF",
    },
    {
        "title": "Actividad 5",
        "color": "#FFBD45",
        "start": "2025-04-21",
        "end": "2025-04-21",
        "resourceId": "PR",
    },
    {
        "title": "Actividad 6",
        "color": "#FF4B4B",
        "start": "2025-04-22",
        "end": "2025-04-22",
        "resourceId": "FT",
    },
    {
        "title": "Actividad 7",
        "color": "#FF4B4B",
        "start": "2025-04-24T08:30:00",
        "end": "2025-04-24T10:30:00",
        "resourceId": "JZ",
    },
]

calendar_resources = [
    {"id": "JZ", "title": "Jonathan Zambrano"},
    {"id": "JF", "title": "Jorge Flores"},
    {"id": "CF", "title": "Christian Flores"},
    {"id": "PR", "title": "Paúl Rengifo"},
    {"id": "FT", "title": "Fabricio Toledo"},
    {"id": "JG", "title": "José Gualoto"},
]

calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "resources": calendar_resources,
    "selectable": "true",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
        }
}

calendar_options = {
            **calendar_options,
            "initialDate": "2025-04-21",
            "initialView": "resourceDayGridDay",
            #"resourceGroupField": "building",
        }

calendar = calendar(
    events= events,
    options=calendar_options,
    #custom_css=custom_css,
    key='calendar', # Assign a widget key to prevent state loss
    )