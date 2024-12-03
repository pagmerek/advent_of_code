const std = @import("std");

pub fn part1(data: []const u8, allocator: std.mem.Allocator) !i32 {
    var first_list = std.ArrayList(i32).init(allocator);
    defer first_list.deinit();

    var second_list = std.ArrayList(i32).init(allocator);
    defer second_list.deinit();

    var it = std.mem.splitScalar(u8, data, '\n');
    while (it.next()) |line| {
        var parsed = std.mem.splitSequence(u8, line, "   ");

        if (parsed.next()) |first_str| {
            if (parsed.next()) |second_str| {
                const first = try std.fmt.parseInt(i32, first_str, 10);
                const second = try std.fmt.parseInt(i32, second_str, 10);

                try first_list.append(@as(i32, first));
                try second_list.append(@as(i32, second));
            }
        }
    }
    std.mem.sort(i32, first_list.items, {}, comptime std.sort.asc(i32));
    std.mem.sort(i32, second_list.items, {}, comptime std.sort.asc(i32));

    var sum: i32 = 0;

    for (first_list.items, second_list.items) |fst, sec| {
        sum += try std.math.absInt(fst - sec);
    }

    return sum;
}

pub fn part2(data: []const u8, allocator: std.mem.Allocator) !i32 {
    var first_list = std.ArrayList(i32).init(allocator);
    defer first_list.deinit();

    var count_map = std.AutoHashMap(i32, i32).init(allocator);
    defer count_map.deinit();

    var it = std.mem.splitScalar(u8, data, '\n');
    while (it.next()) |line| {
        var parsed = std.mem.splitSequence(u8, line, "   ");

        if (parsed.next()) |first_str| {
            if (parsed.next()) |second_str| {
                const first = try std.fmt.parseInt(i32, first_str, 10);
                const second = try std.fmt.parseInt(i32, second_str, 10);

                try first_list.append(first);
                if (count_map.get(second)) |count| {
                    try count_map.put(second, count + 1);
                } else {
                    try count_map.put(second, 1);
                }
            }
        }
    }

    var sum: i32 = 0;

    for (first_list.items) |fst| {
        if (count_map.get(fst)) |count| {
            sum += fst * count;
        }
    }

    return sum;
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

    const result1 = try part1(data[0..], allocator);
    const result2 = try part2(data[0..], allocator);

    try stdout.print("PART 1: {}\nPART 2: {}\n", .{ result1, result2 });

    try bw.flush(); // don't forget to flush!
}

test "test input" {
    const data = @embedFile("test-input.txt");
    const allocator = std.testing.allocator;

    const result1 = try part1(data[0..], allocator);
    const result2 = try part2(data[0..], allocator);
    std.debug.print("TEST PART 1: {}\nTEST PART 2: {}\n", .{ result1, result2 });

    //try std.testing.expectEqual(@as(i32, 42), list.pop());
}
