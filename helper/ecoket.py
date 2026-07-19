# Notes:
import sys
from pathlib import Path
import json
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import Medium, Circle, Event, EventGroup, Source, ReliabilityTypes, OriginTypes, Location

if __name__ == '__main__':
    save_folder_path = Path(__file__).parent.parent
    events_raw: list[Any] = []

    puella = "https://puellabyte.github.io/events"
    main_page = "https://web.archive.org/web/20050204025708/http://eco.ket.jp/page002.html"

    if True: # ==== ecoket 10 ====
        i = 10
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("10_ecoket10.jpg",
                   [Source("https://web.archive.org/web/20070222041308/http://eco.ket.jp:80/ecoket10.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                description="東京・浜松町　都立産業貿易センター２Ｆホール",
                sources=[Source("https://web.archive.org/web/20050204025708/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),  
        ]
        event = Event(
            aliases=["エコケット10 ～ＦＩＮＡＬ～", "EcoKet 10 ~FINAL~"],
            dates="2004.11.03",
            circles=circles_,
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20050204025708/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20070222041448/http://eco.ket.jp:80/ecoket10_clist.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 9 ====
        i = 9
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1-chōme-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="東京・蒲田　大田区産業プラザＰｉｏ大展示ホール",
                sources=[Source("https://web.archive.org/web/20040810060849/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlM30iutkku0DTSgB6rPTEw19CjIMC8icvKceGIJ2eTMqA35cGcD96nMco5OldsWWRdWwEFDXLxoAAXei1t3Zf7GGFGgyWvsUa8bPofUHCGvcxTY3TlJhQNxQFHYYg4fqCFHSE=w408-h544-k-no",
                url="https://maps.app.goo.gl/7ebCWMtzDWoLJQms5",
            ),  
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                description="東京・浜松町　都立産業貿易センター２Ｆ",
                sources=[Source("https://web.archive.org/web/20040810060849/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                comments="Old location before date change.",
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),  
        ]
        event = Event(
            aliases=["エコケット9", "EcoKet 9"],
            dates="2004.05.05 → 2004.05.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Date postponed: https://web.archive.org/web/20040810060849/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20050207073946/http://eco.ket.jp/ecoket9_c_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 8 ====
        i = 8
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("8_ecoket8.jpg",
                   [Source("https://web.archive.org/web/20031212193452/http://eco.ket.jp/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                description="東京・浜松町　都立産業貿易センター２Ｆ",
                sources=[Source("https://web.archive.org/web/20030604192740/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),  
        ]
        event = Event(
            aliases=["エコケット8", "EcoKet 8"],
            dates="2003.10.13",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20050207073559/http://eco.ket.jp/ecoket8_c_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 7 ====
        i = 7
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("7_img003.jpg",
                   [Source("https://web.archive.org/web/20030604192520/http://eco.ket.jp/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                description="東京・浜松町　都立産業貿易センター",
                sources=[Source("https://web.archive.org/web/20030410132005/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),  
        ]
        event = Event(
            aliases=["エコケット7", "EcoKet 7"],
            dates="2003.05.05",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20040724054104/http://eco.ket.jp:80/ecoket7_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 6 ====
        i = 6
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                # comments=None,
                description="東京・浜松町　都立産業貿易センター",
                sources=[Source("https://web.archive.org/web/20020607025109/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),  
        ]
        event = Event(
            aliases=["エコケット6", "EcoKet 6"],
            dates="2002.11.04",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
    #     with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
    #         circles_raw = json.load(f)
    #     event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 5 ====
        i = 5
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                # comments=None,
                description="東京・浜松町　都立産業貿易センター",
                sources=[Source("https://web.archive.org/web/20011217200603/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),  
        ]
        event = Event(
            aliases=["エコケット5", "EcoKet 5"],
            dates="2002.05.05",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
    #     with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
    #         circles_raw = json.load(f)
    #     event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 4 ====
        i = 4
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("4_ecoice_top8.jpg",
                   [Source("https://web.archive.org/web/20010827001039/http://sakura.comike.to:80/ecoket/ecoice_top8.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("4_ecoice_top9.jpg",
                   [Source("https://web.archive.org/web/20050708002450/http://candy-network.org/~ecoket/ecoice_top9.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.698106, 139.790043),
                address="Tōshō Center Bldg., 2 Chome-1-9 Yanagibashi, Taito City, Tokyo 111-0052, Japan",
                description="東京卸商センター３Ｆ",
                sources=[Source("https://web.archive.org/web/20010602194507/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkTmZ2jNL9dQFF6WIjkLAb5tTcTmjIK0VspPB5V_agv8L0jgbo6REvJOi4f1iind4Y7k2Up0RuIAFh0cDH6DRPRs8HfyjxJwINTeZliqpYpUhn_L7w5Qt1j8KChb2qcea7I2IiK=s0?imgmax=0",
                url="https://maps.app.goo.gl/DckJPZaR3gKUijkf6",
            ),
        ]
        event = Event(
            aliases=["エコケット4", "EcoKet 4"],
            dates="2001.11.18",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231003137/http://sakura.comike.to/ecoket/c_list4.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 3 ====
        i = 3
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("3_eco_teleca.jpg",
                   [Source("https://web.archive.org/web/20010826233507/http://sakura.comike.to:80/ecoket/eco_teleca.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            Medium("3_ecoice_top7.jpg",
                   [Source("https://web.archive.org/web/20010826235049/http://sakura.comike.to:80/ecoket/ecoice_top7.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                # comments=None,
                description="東京・浜松町 都立産業貿易センター２Ｆ",
                sources=[Source("https://web.archive.org/web/20001102054729/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),  
        ]
        event = Event(
            aliases=["エコケット3", "EcoKet 3"],
            dates="2001.04.01",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231002259/http://sakura.comike.to/ecoket/c_list3.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 2 ====
        i = 2
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            # Location(
            #     coordinates=(35.655153, 139.7607689),
            #     address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
            #     # comments=None,
            #     description="東京・浜松町 都立産業貿易センター２Ｆ",
            #     sources=[Source("https://web.archive.org/web/20001102054729/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
            #     imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
            #     url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",

            #     description="",
            #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]
            # ),  
        ]
        event = Event(
            aliases=["エコケット2", "EcoKet 2"],
            dates="2000.09.03",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20020217224245/http://sakura.comike.to/ecoket/c_list2.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    if True: # ==== ecoket 1 ====
        i = 1
        name = f"ecoket{i}"
        print(f"Processing {name} ...")

        circles_ = []
        media_ = [
            Medium("1_pic7.gif",
                   [Source("https://web.archive.org/web/20250601191910/https://www.tinami.com/x/riuichi/04/page3.html", (ReliabilityTypes.Likely, OriginTypes.External))]),
            ]
        locations = [
            Location(
                coordinates=(35.6959232, 139.787102),
                address="Japan, 〒111-0052 Tokyo, Taito City, Yanagibashi, 1 Chome−2−10 共和フォーラム 日本",
                description="東京文具共和会館",
                sources=[Source("https://www.tinami.com/x/riuichi/04/page3.html", (ReliabilityTypes.Likely, OriginTypes.External))],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWl41xhdtSFUbvBIJ_pAuMmu26tQ8FBFrz-_JWzVb306EgRIgYV9GyOWC3jLppl3Ts3y--aL8URNYGk0PtGSiydr7LBupNXluFlHp5l3y-gLSqGGihiMPT37Z28oTYnW1w0m3sIQ3SH_xbRG=s0?imgmax=0",
                url="https://maps.app.goo.gl/pL6UGm5dRB4B7Kq17",

            ),  
        ]
        event = Event(
            aliases=["エコケット1", "EcoKet 1"],
            dates="2000.04.23",
            circles=circles_,
            media=media_,
            sources=[
                Source(f"Date: {main_page}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231002137/http://sakura.comike.to/ecoket/c_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
        )
        event_raw = event.get_json()
        with (Path(__file__).parent / "web" / f"{name}" / "all_circles_export.json").open("r", encoding='utf-8') as f:
            circles_raw = json.load(f)
        event_raw["circles"] = circles_raw
        events_raw.append(event_raw)

    # ==== event group ====
    media = [
        Medium("eg_img005.jpg",
               [Source("https://web.archive.org/web/20031212193452/http://eco.ket.jp/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_ecoice_top.jpg",
               [Source("https://web.archive.org/web/20020220045015/http://sakura.comike.to/ecoket/images/ecoice_top.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        Medium("eg_ecoice_top2.jpg",
               [Source("https://web.archive.org/web/20020220045935/http://sakura.comike.to/ecoket/images/ecoice_top2.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["http://eco.ket.jp/index.html", "http://sakura.comike.to/ecoket/", "http://candy-network.org/~ecoket/"]

    event_group = EventGroup(
        aliases=["エコケット", "EcoKet"],
        events=[],
        media=media,
        links=links,
        comments=None,
        description=None,
    )
    
    # Reorder events and add to event group
    events_raw_sorted = sorted(events_raw, key=lambda er: er['dates'])
    
    for event_raw in events_raw_sorted:
        event = Event.load_from_json(event_raw)
        event_group.events.append(event)
    
    print("Saving arts database...")
    event_group.save(save_folder_path, indent=None)

    print("Done")

