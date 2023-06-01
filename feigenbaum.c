#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <cairo.h>

#define WIDTH 800
#define HEIGHT 600
#define NUM_POINTS 1000

void feigenbaum_attractor(double x0, double r_start, double r_end, int num_points, double *r_vals, double *x_vals) {
    double r_step = (r_end - r_start) / num_points;
    double r = r_start;

    for (int i = 0; i < num_points; i++) {
        double x = x0;

        for (int j = 0; j < 100; j++) {
            x = r * x * (1 - x);
        }

        for (int j = 0; j < 200; j++) {
            x = r * x * (1 - x);
            r_vals[i * 200 + j] = r;
            x_vals[i * 200 + j] = x;
        }

        r += r_step;
    }
}

int main() {
    double x_vals[NUM_POINTS * 200];
    double r_vals[NUM_POINTS * 200];
    feigenbaum_attractor(0.5, 2.4, 4.0, NUM_POINTS, r_vals, x_vals);

    cairo_surface_t *surface;
    cairo_t *cr;
    surface = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, WIDTH, HEIGHT);
    cr = cairo_create(surface);

    cairo_set_source_rgb(cr, 1.0, 1.0, 1.0);
    cairo_paint(cr);

    cairo_set_source_rgb(cr, 0.0, 0.0, 0.0);

    for (int i = 0; i < NUM_POINTS * 200; i++) {
        double x = r_vals[i];
        double y = x_vals[i];

        int screen_x = WIDTH * (x - 2.4) / (4.0 - 2.4);
        int screen_y = HEIGHT - HEIGHT * y;

        cairo_rectangle(cr, screen_x, screen_y, 1, 1);
        cairo_fill(cr);
    }

    cairo_surface_write_to_png(surface, "feigenbaum.png");

    cairo_destroy(cr);
    cairo_surface_destroy(surface);

    return 0;
}
