from gps import*
session = gps()
session.stream(WATCH_ENABLE|WATCH_NEWSTYLE)

counter = 0
while counter < 50:
        report = session.next()
        if report.keys()[0] == 'epx' :
                lat = float(report['lat'])
                lon = float(report['lon'])
                alt = float(report['alt'])
                print("lat=%f\tlon=%f\ttime=%s\talt=%f" % (lat, lon, report['time'], alt))
                time.sleep(0.5)
        counter = counter + 1
