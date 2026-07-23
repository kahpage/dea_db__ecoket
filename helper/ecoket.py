# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    active_events: list[int | str] = list(range(1, 14 + 1))

    main_dates_url = "https://web.archive.org/web/20050204025708/http://eco.ket.jp/page002.html"

    i = 1  # ==== ecoket1 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

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
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231002137/http://sakura.comike.to/ecoket/c_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== ecoket2 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            # Location(
            #     coordinates=(,),
            #     address="",
            #     description="",
            #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
            #     # comments=None,
            #     imageUrl="",
            #     url="",
            # ),  
        ]
        event = Event(
            aliases=[f"エコケット{i}", f"EcoKet {i}"],
            dates="2000.09.03",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20020217224245/http://sakura.comike.to/ecoket/c_list2.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== ecoket3 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

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
                comments=None,
                description="東京・浜松町 都立産業貿易センター２Ｆ",
                sources=[Source("https://web.archive.org/web/20001102054729/http://sakura.comike.to/ecoket/ecoket.htm", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),  
        ]
        event = Event(
            aliases=[f"エコケット{i}", f"EcoKet {i}"],
            dates="2001.04.01",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231002259/http://sakura.comike.to/ecoket/c_list3.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== ecoket4 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

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
            aliases=[f"エコケット{i}", f"EcoKet {i}"],
            dates="2001.11.18",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20011231003137/http://sakura.comike.to/ecoket/c_list4.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 5  # ==== ecoket5 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
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
            aliases=[f"エコケット{i}", f"EcoKet {i}"],
            dates="2002.05.05",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 6  # ==== ecoket6 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
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
            aliases=[f"エコケット{i}", f"EcoKet {i}"],
            dates="2002.11.04",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 7  # ==== ecoket7 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("7_img003.jpg",
                   [Source("https://web.archive.org/web/20030604192520/http://eco.ket.jp/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
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
            aliases=[f"エコケット{i}", f"EcoKet {i}"],
            dates="2003.05.05",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20040724054104/http://eco.ket.jp:80/ecoket7_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 8  # ==== ecoket8 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("8_ecoket8.jpg",
                   [Source("https://web.archive.org/web/20031212193452/http://eco.ket.jp/index.html", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
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
            aliases=[f"エコケット{i}", f"EcoKet {i}"],
            dates="2003.10.13",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20050207073559/http://eco.ket.jp/ecoket8_c_list.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 9  # ==== ecoket9 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
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
            aliases=[f"エコケット{i}", f"EcoKet {i}"],
            dates="2004.05.05 → 2004.05.23",
            circles=[],
            media=media_,
            sources=[
                Source(f"Date: {main_dates_url}", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Date postponed: https://web.archive.org/web/20040810060849/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20050207073946/http://eco.ket.jp/ecoket9_c_list.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 10  # ==== ecoket10 ====
    if i in active_events:
        event_name = f"ecoket{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("10_ecoket10.jpg",
                   [Source("https://web.archive.org/web/20070222041308/http://eco.ket.jp:80/ecoket10.jpg", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
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
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20050204025708/http://eco.ket.jp/page002.html", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20070222041448/http://eco.ket.jp:80/ecoket10_clist.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.07.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

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
        events=events,
        media=media,
        links=links,
        sources=[
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments=None,
        description=None,
        last_edited="2026.07.23",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
