module fir_filter_weighted (
    input clk,
    input signed [15:0] in_sample,
    output wire signed [35:0] out_sample
);

    // flip flop for holding past values
    reg signed [15:0] x0=16'd0, x1=16'd0, x2=16'd0, x3=16'd0, x4=16'd0, x5=16'd0, x6=16'd0, x7=16'd0, x8=16'd0, x9=16'd0, x10=16'd0, x11=16'd0, x12=16'd0, x13=16'd0, x14=16'd0, x15=16'd0;

    // Coefficients for the filter
    reg signed [15:0] h0 = 16'b1111110110110010; // -0.01800537109375
    reg signed [15:0] h1 = 16'b1111110101001001; // -0.021209716796875
    reg signed [15:0] h2 = 16'b1111111010010000; // -0.01123046875
    reg signed [15:0] h3 = 16'b0000001000110000; // 0.01708984375
    reg signed [15:0] h4 = 16'b0000100000001001; // 0.062774658203125
    reg signed [15:0] h5 = 16'b0000111100000000; // 0.1171875
    reg signed [15:0] h6 = 16'b0001010101000110; // 0.16619873046875
    reg signed [15:0] h7 = 16'b0001100011111111; // 0.195281982421875
    reg signed [15:0] h8 = 16'b0001100011111111; // 0.195281982421875
    reg signed [15:0] h9 = 16'b0001010101000110; // 0.16619873046875
    reg signed [15:0] h10 = 16'b0000111100000000; // 0.1171875
    reg signed [15:0] h11 = 16'b0000100000001001; // 0.062774658203125
    reg signed [15:0] h12 = 16'b0000001000110000; // 0.01708984375
    reg signed [15:0] h13 = 16'b1111111010010000; // -0.01123046875
    reg signed [15:0] h14 = 16'b1111110101001001; // -0.021209716796875
    reg signed [15:0] h15 = 16'b1111110110110010; // -0.01800537109375

    // Registers to store multiplication results
    wire signed [31:0] m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15;

    // Multiply inputs with coefficients
    assign m0 = $signed(h0) * $signed(x0);
    assign m1 = $signed(h1) * $signed(x1);
    assign m2 = $signed(h2) * $signed(x2);
    assign m3 = $signed(h3) * $signed(x3);
    assign m4 = $signed(h4) * $signed(x4);
    assign m5 = $signed(h5) * $signed(x5);
    assign m6 = $signed(h6) * $signed(x6);
    assign m7 = $signed(h7) * $signed(x7);
    assign m8 = $signed(h8) * $signed(x8);
    assign m9 = $signed(h9) * $signed(x9);
    assign m10 = $signed(h10) * $signed(x10);
    assign m11 = $signed(h11) * $signed(x11);
    assign m12 = $signed(h12) * $signed(x12);
    assign m13 = $signed(h13) * $signed(x13);
    assign m14 = $signed(h14) * $signed(x14);
    assign m15 = $signed(h15) * $signed(x15);

    // Sum the products to get the output sample
    assign out_sample = m0 + m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11 + m12 + m13 + m14 + m15;

    // Shift registers to hold past samples
    always @(posedge clk) begin
        x15 <= x14;
        x14 <= x13;
        x13 <= x12;
        x12 <= x11;
        x11 <= x10;
        x10 <= x9;
        x9 <= x8;
        x8 <= x7;
        x7 <= x6;
        x6 <= x5;
        x5 <= x4;
        x4 <= x3;
        x3 <= x2;
        x2 <= x1;
        x1 <= x0;
        x0 <= in_sample;
    end

endmodule
