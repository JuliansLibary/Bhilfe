// Cone-Rolling-Tool P0 -- OpenSCAD 2021.01 or newer, millimetres.
// Experimental mandrel + open loading/rest station. No automatic paper feed.
// F5: preview. Select ONE print part, F6: render, then export STL.

/* [Ansicht und Format] */
part = "assembly"; // [assembly:Baugruppe, mandrel:Formdorn in Drucklage, station:Anlegestation, print_layout:Beide Teile in Drucklage]
paper_format = "one_quarter"; // [one_quarter:1 1/4 - angenommen 78 x 44 mm, king_size_slim:King Size Slim - angenommen 110 x 44 mm]

/* [Papier und Zielgeometrie] */
// 0 uses the selected format's length. Measure actual paper before printing.
paper_length_override_mm = 0; // [0:0.5:150]
paper_width_mm = 44; // [30:0.5:80]
glue_width_mm = 4; // [1:0.5:8]
// 0 uses a 68/98 mm fully enclosed target zone, NOT total finished paper length.
zone_length_override_mm = 0; // [0:0.5:140]
small_diameter_mm = 6; // [3:0.1:12]
large_diameter_mm = 12; // [7:0.1:22]

/* [Druck und Handhabung] */
// Diameter clearance, not radial clearance.
journal_clearance_mm = 0.5; // [0.2:0.1:1]
grip_diameter_mm = 24; // [20:1:32]
grip_length_mm = 24; // [18:1:32]
base_thickness_mm = 3; // [2.4:0.2:5]
contact_edge_radius_mm = 0.4; // [0.2:0.1:0.8]
quality = "normal"; // [normal:Normal, fine:Fein]

/* [Hidden] */
eps = 0.02;
is_short = paper_format == "one_quarter";
paper_length = paper_length_override_mm > 0 ? paper_length_override_mm
               : (is_short ? 78 : 110);
zone_length = zone_length_override_mm > 0 ? zone_length_override_mm
              : (is_short ? 68 : 98);
r0 = small_diameter_mm / 2;
r1 = large_diameter_mm / 2;
dr = r1 - r0;
slant = sqrt(zone_length * zone_length + dr * dr);
// OpenSCAD trigonometric functions use DEGREES.
alpha = atan(dr / zone_length);
sector_angle = 360 * dr / slant;
developed_r0 = r0 * slant / dr;
developed_r1 = r1 * slant / dr;
required_length = developed_r1 - developed_r0 * cos(sector_angle);
required_width = developed_r1 * sin(sector_angle) + glue_width_mm;
paper_x0 = developed_r0 * cos(sector_angle)
           - (paper_length - required_length) / 2;
paper_max_y = max(glue_width_mm, paper_width_mm - glue_width_mm);
paper_rho_max = sqrt(pow(paper_x0 + paper_length, 2) + pow(paper_max_y, 2));
paper_z_min = (paper_x0 - developed_r0) * cos(alpha);
paper_z_max = (paper_rho_max - developed_r0) * cos(alpha);
end_allowance = 2;
minimum_core_length = paper_z_max - paper_z_min + 2 * end_allowance;
core_length = ceil(minimum_core_length / 10) * 10;
extra_length = core_length - minimum_core_length;
core_zone_start_z = paper_z_min - end_allowance - extra_length / 2;
core_small_r = r0 + core_zone_start_z * dr / zone_length;
core_large_r = core_small_r + core_length * dr / zone_length;
journal_length = 20;
journal_r = max(7, core_large_r + contact_edge_radius_mm + 0.2);
grip_r = grip_diameter_mm / 2;
total_length = core_length + journal_length + grip_length_mm;
post_width = 4;
post_wall = 3;
bore_r = journal_r + journal_clearance_mm / 2;
post_half_width = bore_r + post_wall;
axis_height = max(20, base_thickness_mm + core_large_r + 3,
                  base_thickness_mm + grip_r + 2);
post_top = axis_height + 3;
base_margin = 6;
base_x_min = -base_margin;
base_x_max = core_length + journal_length + 4;
base_length = base_x_max - base_x_min;
base_width = max(paper_width_mm + 16, 2 * post_half_width + 8);
base_corner_r = 3;
circle_segments = quality == "fine" ? 240 : 128;
round_segments = quality == "fine" ? 64 : 32;
$fn = circle_segments;

assert(part == "assembly" || part == "mandrel" || part == "station"
       || part == "print_layout", "Unknown part selection");
assert(paper_format == "one_quarter" || paper_format == "king_size_slim",
       "Unknown paper format");
assert(quality == "normal" || quality == "fine", "Unknown quality setting");
assert(paper_length_override_mm >= 0 && zone_length_override_mm >= 0,
       "Length overrides must be 0 (automatic) or positive");
assert(zone_length > 0 && paper_length > 0 && r0 > 0 && dr > 0,
       "Require positive lengths and large diameter > small diameter");
assert(glue_width_mm > 0 && paper_width_mm > glue_width_mm,
       "Paper must be wider than its positive glue strip");
assert(sector_angle < 90 && paper_x0 > 0,
       "Geometry outside this shallow-cone development model");
assert(paper_length >= required_length && paper_width_mm >= required_width,
       str("Paper too small: need at least ", required_length, " x ",
           required_width, " mm for this target zone and glue strip"));
assert(contact_edge_radius_mm > 0 && core_small_r > 2 * contact_edge_radius_mm,
       "Edge rounding too large for small end");
assert(journal_clearance_mm > 0 && journal_clearance_mm <= 2,
       "Use a positive diameter clearance no larger than 2 mm");
assert(grip_r > journal_r + contact_edge_radius_mm
       && grip_length_mm > 4 * contact_edge_radius_mm,
       "Grip must be wider than the journal and long enough to round");
assert(base_thickness_mm >= 2 && base_thickness_mm < axis_height - bore_r,
       "Invalid base thickness");

echo(format = paper_format,
     target_zone_mm = zone_length,
     half_angle_degrees = alpha,
     required_paper_mm = [required_length, required_width],
     forming_length_mm = core_length,
     complete_mandrel_length_mm = total_length,
     actual_core_end_diameters_mm = [2 * core_small_r, 2 * core_large_r]);

// Profile is extended LEFT of the rotation axis before rounding. Clipping it
// back at x=0 keeps both end faces closed and avoids a central end-face dimple.
module mandrel_profile() {
    intersection() {
        translate([0, -1])
            square([grip_r + journal_r + 2, total_length + 2]);
        offset(r = contact_edge_radius_mm, $fn = round_segments)
            offset(delta = -contact_edge_radius_mm)
                polygon([
                    [-2, 0],
                    [core_small_r, 0],
                    [core_large_r, core_length],
                    [journal_r, core_length],
                    [journal_r, core_length + journal_length],
                    [grip_r, core_length + journal_length],
                    [grip_r, total_length],
                    [-2, total_length]
                ]);
    }
}

// Local z=0 is the free small tip; grip is at the positive end.
module mandrel_local() {
    rotate_extrude(convexity = 10)
        mandrel_profile();
}

// Broad grip face down; no support on the paper-contacting cone surface.
module mandrel_print() {
    translate([0, 0, total_length])
        rotate([180, 0, 0])
            mandrel_local();
}

module rounded_base() {
    linear_extrude(height = base_thickness_mm)
        hull()
            for (x = [base_x_min + base_corner_r, base_x_max - base_corner_r])
                for (y = [-base_width / 2 + base_corner_r,
                           base_width / 2 - base_corner_r])
                    translate([x, y])
                        circle(r = base_corner_r, $fn = round_segments);
}

// Open upward: circular lower rest plus a full-height rectangular escape slot.
// The supports touch ONLY the wide-end journal, never the forming surface.
module journal_post(x) {
    difference() {
        translate([x, -post_half_width, base_thickness_mm - eps])
            cube([post_width, 2 * post_half_width,
                  post_top - base_thickness_mm + eps]);
        translate([x - eps, 0, axis_height])
            rotate([0, 90, 0])
                cylinder(h = post_width + 2 * eps, r = bore_r);
        translate([x - eps, -bore_r, axis_height])
            cube([post_width + 2 * eps, 2 * bore_r, post_top + eps]);
    }
}

module station_local() {
    union() {
        rounded_base();
        journal_post(core_length + 3);
        journal_post(core_length + journal_length - 7);
    }
}

module station_print() {
    translate([-base_x_min, base_width / 2, 0])
        station_local();
}

// The horizontal tray is BELOW the cone, not a tangent nip/rolling channel.
// Lift the mandrel out for wrapping and extraction. The display shows the
// nominal journal centre; the printed clearance lets it settle slightly lower.
module assembly() {
    color([0.80, 0.83, 0.87]) station_local();
    color([0.12, 0.47, 0.63])
        translate([0, 0, axis_height])
            rotate([0, 90, 0])
                mandrel_local();
}

module print_layout() {
    color([0.80, 0.83, 0.87]) station_print();
    color([0.12, 0.47, 0.63])
        translate([grip_r + 5, base_width + grip_r + 8, 0])
            mandrel_print();
}

// Model dispatch. STL export should normally select exactly one print part.
if (part == "mandrel") mandrel_print();
else if (part == "station") station_print();
else if (part == "print_layout") print_layout();
else assembly();
