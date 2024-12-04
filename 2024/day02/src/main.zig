const std = @import("std");

const LevelType = enum { increasing, decreasing };

fn isUnsafe(bigger: i32, smaller: i32) bool {
    return bigger - smaller > 3 or bigger - smaller < 1;
}

fn scanLevel(records: []const i32, levelType: LevelType) struct { isSafe: bool, errorAt: ?usize } {
    var errorAt: ?usize = null;
    var isSafe: bool = true;
    var i: usize = 0;
    while (i < records.len - 1) : (i += 1) {
        switch (levelType) {
            .increasing => if (isUnsafe(records[i + 1], records[i])) {
                errorAt = i;
                isSafe = false;
                break;
            },
            .decreasing => if (isUnsafe(records[i], records[i + 1])) {
                errorAt = i;
                isSafe = false;
                break;
            },
        }
    }
    return .{ .isSafe = isSafe, .errorAt = errorAt };
}

pub fn part1(data: []const u8, allocator: std.mem.Allocator) !i32 {
    var safeLevelCount: i32 = 0;

    var it = std.mem.splitScalar(u8, data, '\n');
    while (it.next()) |report| {
        if (report.len == 0) break;

        var list = std.ArrayList(i32).init(allocator);
        defer list.deinit();

        var parsed = std.mem.splitScalar(u8, report, ' ');

        while (parsed.next()) |level| {
            const parsedLevel = try std.fmt.parseInt(i32, level, 10);
            try list.append(parsedLevel);
        }

        const records = list.items;

        const levelType: LevelType =
            if (records[0] < records[1]) .increasing else .decreasing;

        const result = scanLevel(records, levelType);
        if (result.isSafe) {
            safeLevelCount += 1;
        }
    }

    return safeLevelCount;
}

pub fn part2(data: []const u8, allocator: std.mem.Allocator) !i32 {
    var safeLevelCount: i32 = 0;

    var it = std.mem.splitScalar(u8, data, '\n');
    while (it.next()) |report| {
        if (report.len == 0) break;

        var list = std.ArrayList(i32).init(allocator);
        defer list.deinit();

        var parsed = std.mem.splitScalar(u8, report, ' ');

        while (parsed.next()) |level| {
            const parsedLevel = try std.fmt.parseInt(i32, level, 10);
            try list.append(parsedLevel);
        }

        const records = list.items;

        var i: usize = 0;
        var increasing: i32 = 0;
        var decreasing: i32 = 0;
        while (i < records.len - 1) : (i += 1) {
            if (records[i] <= records[i + 1]) {
                increasing += 1;
            }
            if (records[i] >= records[i + 1]) {
                decreasing += 1;
            }
        }

        const levelType: LevelType =
            if (decreasing < increasing) .increasing else .decreasing;

        var result = scanLevel(records, levelType);

        const errorAt = result.errorAt;
        if (errorAt != null) {
            var records1 = try list.clone();
            defer records1.deinit();

            _ = records1.orderedRemove(result.errorAt.?);

            const recordsWithoutFirst = records1.items;

            result = scanLevel(recordsWithoutFirst, levelType);

            if (result.isSafe != true) {
                var records2 = try list.clone();
                defer records2.deinit();

                _ = records2.orderedRemove(errorAt.? + 1);

                const recordsWithoutSecond = records2.items;
                result = scanLevel(recordsWithoutSecond, levelType);
            }
        }

        if (result.isSafe) {
            safeLevelCount += 1;
        }
    }

    return safeLevelCount;
}

pub fn main() !void {
    const file = std.fs.cwd().openFile("full-input.txt", .{}) catch |err| {
        std.log.err("Failed to open file: {s}", .{@errorName(err)});
        return;
    };
    defer file.close();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();
    defer _ = gpa.deinit();

    const data = file.readToEndAlloc(allocator, std.math.maxInt(usize)) catch |err| {
        std.log.err("Failed to read file: {s}", .{@errorName(err)});
        return;
    };

    defer allocator.free(data);

    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    var timer = try std.time.Timer.start();

    const result1 = try part1(data[0..], allocator);
    const time1 = timer.read() / std.time.ns_per_ms;

    timer.reset();
    const result2 = try part2(data[0..], allocator);
    const time2 = timer.read() / std.time.ns_per_ms;

    try stdout.print("PART 1: {} TIME: {}ms\nPART 2: {} TIME: {}ms\n", .{ result1, time1, result2, time2 });

    try bw.flush();
}

test "test input" {
    const data = @embedFile("test-input.txt");
    const allocator = std.testing.allocator;

    const result1 = try part1(data[0..], allocator);
    const result2 = try part2(data[0..], allocator);
    std.debug.print("TEST PART 1: {}\nTEST PART 2: {}\n", .{ result1, result2 });
}

test "edgecases input for part 2" {
    const allocator = std.testing.allocator;

    const data =
        \\48 46 47 49 51 54 56
        \\1 1 2 3 4 5
        \\1 2 3 4 5 5
        \\5 1 2 3 4 5
        \\1 4 3 2 1
        \\1 6 7 8 9
        \\1 2 3 4 3
        \\9 8 7 6 7
        \\7 10 8 10 11
        \\29 28 27 25 26 25 22 20
    ;
    const result = try part2(data[0..], allocator);
    try std.testing.expect(result == 10);
}
