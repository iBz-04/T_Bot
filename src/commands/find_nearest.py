from telegram import Update
from telegram.ext import CallbackContext
from data_loader import get_data
from utils.geo import haversine

def find_nearest(update: Update, context: CallbackContext):
    loc = update.message.location
    args = context.args
    # Shared location
    if loc:
        lat, lon = loc.latitude, loc.longitude
    # Numeric lat/lon args
    elif len(args) == 2:
        try:
            lat, lon = float(args[0]), float(args[1])
        except ValueError:
            # Treat as mahalle name
            mahalle = ' '.join(args)
            df = get_data()
            matches = df[df['MAHALLE ADI'].str.contains(mahalle, case=False)]
            if matches.empty:
                update.message.reply_text(f"'{mahalle}' mahallesi bulunamadı.")
            else:
                lines = [f"{r['name']} ({r['lat']:.6f}, {r['lon']:.6f})" for _, r in matches.iterrows()]
                update.message.reply_text(f"{mahalle} Mahallesi toplanma alanları:\n" + "\n".join(lines))
            return
    # Mahalle name lookup
    elif len(args) >= 1:
        mahalle = ' '.join(args)
        df = get_data()
        matches = df[df['MAHALLE ADI'].str.contains(mahalle, case=False)]
        if matches.empty:
            update.message.reply_text(f"'{mahalle}' mahallesi bulunamadı.")
        else:
            lines = [f"{r['name']} ({r['lat']:.6f}, {r['lon']:.6f})" for _, r in matches.iterrows()]
            update.message.reply_text(f"{mahalle} Mahallesi toplanma alanları:\n" + "\n".join(lines))
        return
    # Usage message
    else:
        update.message.reply_text("Kullanım: /find_nearest <enlem> <boylam> veya mahalle adı girin ya da konum paylaşın")
        return
    df = get_data()
    df['distance'] = df.apply(lambda row: haversine(lat, lon, row['lat'], row['lon']), axis=1)
    nearest = df.loc[df['distance'].idxmin()]
    name = nearest['name']
    dist = nearest['distance']
    update.message.reply_text(f"En yakın nokta: {name} ({dist:.2f} km)")
