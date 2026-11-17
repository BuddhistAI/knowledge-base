// Map of Buddhists by country for the Languages page.
// Needs d3 and topojson-client (loaded on the page) and the JSON block #buddhist-map-data written by scripts/build.py.
// Colors are design-system variables mixed with the surface color, so light and dark mode both work.
(function () {
  var box = document.getElementById("buddhist-map");
  var dataEl = document.getElementById("buddhist-map-data");
  if (!box || !dataEl || !window.d3 || !window.topojson) return;
  var rows = JSON.parse(dataEl.textContent);
  var byIso = {};
  rows.forEach(function (r) { byIso[r.iso] = r; });
  // five steps of one hue (lapis), light to dark
  var bins = [1e6, 5e6, 20e6, 50e6];
  var mixes = [28, 45, 62, 80, 100];
  var names = ["under 1 million", "1 to 5 million", "5 to 20 million", "20 to 50 million", "50 million or more"];
  function step(n) { var i = 0; while (i < bins.length && n >= bins[i]) i++; return i; }
  function fill(i) { return "color-mix(in oklab, var(--lapis) " + mixes[i] + "%, var(--surface))"; }
  function fmt(n) {
    return n >= 1e6 ? (Math.round(n / 1e5) / 10) + " million" : n.toLocaleString("en");
  }

  d3.json("https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-50m.json").then(function (world) {
    var all = topojson.feature(world, world.objects.countries);
    var w = 760, h = 470;
    var focus = { type: "Feature", geometry: { type: "Polygon", coordinates: [[[62, -2], [62, 56], [148, 56], [148, -2], [62, -2]]] } };
    var proj = d3.geoMercator().fitExtent([[8, 8], [w - 8, h - 8]], focus);
    var path = d3.geoPath(proj);
    var svg = d3.select(box).append("svg").attr("viewBox", "0 0 " + w + " " + h).attr("class", "chart");
    var tip = d3.select(box).append("div").attr("class", "map-tip").attr("hidden", true);
    svg.append("g").selectAll("path").data(all.features).join("path")
      .attr("d", path)
      .attr("class", function (d) { return byIso[d.id] ? "country has" : "country"; })
      .style("fill", function (d) { var r = byIso[d.id]; return r ? fill(step(r.n)) : null; })
      .on("mousemove", function (ev, d) {
        var r = byIso[d.id];
        if (!r) { tip.attr("hidden", true); return; }
        var b = box.getBoundingClientRect();
        tip.attr("hidden", null).html("<b>" + r.name + "</b><br>" + fmt(r.n) + " Buddhists<br><span>" + r.label + "</span>")
          .style("left", (ev.clientX - b.left + 14) + "px").style("top", (ev.clientY - b.top + 14) + "px");
      })
      .on("mouseleave", function () { tip.attr("hidden", true); })
      .append("title").text(function (d) { var r = byIso[d.id]; return r ? r.name + ": " + fmt(r.n) + " Buddhists" : ""; });
    // small places get a ring so they can be found and hovered
    rows.filter(function (r) { return ["702", "344", "064"].indexOf(r.iso) >= 0; }).forEach(function (r) {
      var f = all.features.find(function (d) { return d.id === r.iso; });
      if (!f) return;
      var c = proj(d3.geoCentroid(f));
      svg.append("circle").attr("cx", c[0]).attr("cy", c[1]).attr("r", 6).attr("class", "ring")
        .style("fill", fill(step(r.n))).append("title").text(r.name + ": " + fmt(r.n) + " Buddhists");
    });
    var lg = d3.select(box).append("div").attr("class", "map-legend");
    lg.append("span").attr("class", "lg-title").text("Buddhists");
    names.forEach(function (t, i) {
      var item = lg.append("span").attr("class", "lg-item");
      item.append("i").style("background", fill(i));
      item.append("span").text(t);
    });
  }).catch(function () {
    box.innerHTML = "<p class=\"note\">The map could not load. The numbers are in the table below.</p>";
  });
})();
