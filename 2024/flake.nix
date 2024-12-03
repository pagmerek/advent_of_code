{
  description = "Zig dev flake";

  inputs.nixpkgs.url = "github:nixos/nixpkgs";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils}:
    let
    in
      flake-utils.lib.eachDefaultSystem (
        system:
          let
            pkgs' = import nixpkgs { inherit system; };
          in
            rec {
              devShell = pkgs'.mkShell {
                nativeBuildInputs = [];
                buildInputs = with pkgs'; [];
                packages = with pkgs'; [ 
                    zig
                    zls
                ];

               # shellHook = ''
               # PATH="${pkgs'.clang-tools}/bin:$PATH"
               # '';
              };
            }
      );
}
