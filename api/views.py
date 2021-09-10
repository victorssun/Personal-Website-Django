from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter, DateFilter

from .models import MonthlySummary, Transactions
from .models import Positions, Trades, Transfers

from .serializers import IncomeSerializer, TransactionsSerializer
from .serializers import PositionsSerializer, TradesSerializer, TransfersSerializer

from drf_spectacular.utils import extend_schema


class TransactionSetFilter(FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    min_amount = NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Transactions
        fields = [
            "start_date",
            "end_date",
            "date",
            "category",
            "location",
            "min_amount",
            "max_amount",
        ]


class PositionsSetFilter(FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    min_amount = NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Positions
        fields = [
            "start_date",
            "end_date",
            "date",
            "symbol",
            "min_amount",
            "max_amount",
        ]


class TradesSetFilter(FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    min_amount = NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Trades
        fields = [
            "start_date",
            "end_date",
            "date",
            "symbol",
            "min_amount",
            "max_amount",
        ]


class TransfersSetFilter(FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    min_amount = NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Transfers
        fields = [
            "start_date",
            "end_date",
            "date",
            "min_amount",
            "max_amount",
        ]


class IncomeSet(viewsets.ModelViewSet):
    queryset = MonthlySummary.objects.all()
    serializer_class = IncomeSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['date']
    filterset_fields = ['date']
    ordering_fields = ['date', 'income', 'cashback', 'interest', 'investment']

    @extend_schema(description='Retrieve list of monthly income streams. Can filter/search/order response.', methods=["GET"])
    def list(self, request):
        return super().list(request)

    @extend_schema(description='Create new instance of monthly income streams', methods=["POST"])
    def create(self, request):
        return super().create(request)

    @extend_schema(description='Retrieve details of a monthly income stream', methods=["GET"])
    def retrieve(self, request):
        return super().retrieve(request)

    @extend_schema(description='Update details of a monthly income stream', methods=["PUT"])
    def update(self, request):
        return super().update(request)

    @extend_schema(description='Partially update details of a monthly income stream', methods=["PATCH"])
    def partial_update(self, request):
        return super().partial_update(request)

    @extend_schema(description='Remove an instance of monthly streams', methods=["DELETE"])
    def destroy(self, request):
        return super().destroy(request)


class TransactionsSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['date', 'description', 'category', 'location']
    ordering_fields = ['date', 'amount']
    filterset_class = TransactionSetFilter

    @extend_schema(description='Retrieve list of transactions (expenses). Can filter/search/order response.', methods=["GET"])
    def list(self, request):
        return super().list(request)

    @extend_schema(description='Create new instance of a transaction', methods=["POST"])
    def create(self, request):
        return super().create(request)

    @extend_schema(description='Retrieve details of a transaction', methods=["GET"])
    def retrieve(self, request):
        return super().retrieve(request)

    @extend_schema(description='Update details of a transaction', methods=["PUT"])
    def update(self, request):
        return super().update(request)

    @extend_schema(description='Partially update details of a transaction', methods=["PATCH"])
    def partial_update(self, request):
        return super().partial_update(request)

    @extend_schema(description='Remove an instance of a transaction', methods=["DELETE"])
    def destroy(self, request):
        return super().destroy(request)


class PositionsSet(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['date', 'symbol']
    ordering_fields = ['date', 'value']
    filterset_class = PositionsSetFilter

    @extend_schema(description='Retrieve list of investment positions. Can filter/search/order response.', methods=["GET"])
    def list(self, request):
        return super().list(request)

    @extend_schema(description='Create new instance of a position', methods=["POST"])
    def create(self, request):
        return super().create(request)

    @extend_schema(description='Retrieve details of a position', methods=["GET"])
    def retrieve(self, request):
        return super().retrieve(request)

    @extend_schema(description='Update details of a position', methods=["PUT"])
    def update(self, request):
        return super().update(request)

    @extend_schema(description='Partially update details of a position', methods=["PATCH"])
    def partial_update(self, request):
        return super().partial_update(request)

    @extend_schema(description='Remove an instance of a position', methods=["DELETE"])
    def destroy(self, request):
        return super().destroy(request)


class TradesSet(viewsets.ModelViewSet):
    queryset = Trades.objects.all()
    serializer_class = TradesSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['date', 'symbol']
    ordering_fields = ['date', 'value']
    filterset_class = TradesSetFilter

    @extend_schema(description='Retrieve list of investment trades. Can filter/search/order response.', methods=["GET"])
    def list(self, request):
        return super().list(request)

    @extend_schema(description='Create new instance of a trade', methods=["POST"])
    def create(self, request):
        return super().create(request)

    @extend_schema(description='Retrieve details of a trade', methods=["GET"])
    def retrieve(self, request):
        return super().retrieve(request)

    @extend_schema(description='Update details of a trade', methods=["PUT"])
    def update(self, request):
        return super().update(request)

    @extend_schema(description='Partially update details of a trade', methods=["PATCH"])
    def partial_update(self, request):
        return super().partial_update(request)

    @extend_schema(description='Remove an instance of a trade', methods=["DELETE"])
    def destroy(self, request):
        return super().destroy(request)


class TransfersSet(viewsets.ModelViewSet):
    queryset = Transfers.objects.all()
    serializer_class = TransfersSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['date']
    ordering_fields = ['date', 'amount']
    filterset_class = TransfersSetFilter

    @extend_schema(description='Retrieve list of account transfers (deposits and withrawals). Can filter/search/order response.', methods=["GET"])
    def list(self, request):
        return super().list(request)

    @extend_schema(description='Create new instance of a transfer', methods=["POST"])
    def create(self, request):
        return super().create(request)

    @extend_schema(description='Retrieve details of a transfer', methods=["GET"])
    def retrieve(self, request):
        return super().retrieve(request)

    @extend_schema(description='Update details of a transfer', methods=["PUT"])
    def update(self, request):
        return super().update(request)

    @extend_schema(description='Partially update details of a transfer', methods=["PATCH"])
    def partial_update(self, request):
        return super().partial_update(request)

    @extend_schema(description='Remove an instance of a transfer', methods=["DELETE"])
    def destroy(self, request):
        return super().destroy(request)
